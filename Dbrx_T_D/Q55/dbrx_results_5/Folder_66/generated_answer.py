from itertools import islice, cycle

def lists_with_product_equal_n(numbers, n=78):

    def contiguous_sublists(numbers):
        for size in range(1, len(numbers) + 1):
            for start in range(len(numbers) - size + 1):
                yield numbers[start:start + size]

    def product_equal_to_n(sublist):
        return n == 0 or (n > 0 and all((number != 0 for number in sublist)) and (n % reduce(lambda p, x: p * x, sublist) == 0))

    def circular_sublists(numbers):
        circular = list(numbers)
        circular.extend(numbers)
        return islice(circular, len(numbers) - 1, None)
    return [sublist for sublist in circular_sublists(numbers) if product_equal_to_n(sublist)]