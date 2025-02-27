from itertools import islice, cycle

def lists_with_product_equal_n(numbers, n):

    def sublists_with_product_equal_n(numbers, n, start=0):
        for i in range(start, len(numbers)):
            sublist = list(islice(cycle(numbers), i, i + len(numbers)))
            if n == 1 and sublist == [1]:
                yield [1]
            elif n == -1 and sublist == [-1]:
                yield [-1]
            elif prod(sublist) == n:
                yield sublist

    def prod(numbers):
        result = 1
        for number in numbers:
            result *= number
        return result
    return list(set(sublists_with_product_equal_n(numbers, n)))