from itertools import islice

def lists_with_product_equal_n(numbers, n=8):

    def circular_sublists(numbers):
        for i in range(len(numbers)):
            yield (numbers[i:] + numbers[:i])

    def product(numbers):
        return reduce(lambda x, y: x * y, numbers, 1)
    return [sublist for sublist in circular_sublists(numbers) if product(sublist) == n]