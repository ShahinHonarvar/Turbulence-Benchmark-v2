from itertools import islice, cycle

def lists_with_product_equal_n(numbers, n=76):

    def sublists_with_product_equal_n(numbers, n):
        for size in range(1, len(numbers) + 1):
            for i in range(len(numbers) - size + 1):
                sublist = numbers[i:i + size]
                if n == 1 and (not sublist):
                    yield []
                elif not sublist:
                    continue
                elif prod(sublist) == n:
                    yield sublist
                elif prod(sublist) < n:
                    yield from sublists_with_product_equal_n(sublist, n // prod(sublist))

    def prod(numbers):
        result = 1
        for num in numbers:
            result *= num
        return result
    return list(set(sublists_with_product_equal_n(cycle(numbers), n)))