from itertools import islice, cycle

def lists_with_product_equal_n(numbers):

    def sublists_with_product_equal_n(numbers, n):
        for i in range(1, len(numbers) + 1):
            for j in range(len(numbers)):
                sublist = list(islice(cycle(numbers), j, j + i))
                if len(sublist) > 1 and prod(sublist) == n:
                    yield sublist

    def prod(numbers):
        result = 1
        for number in numbers:
            result *= number
        return result
    return list(set(sublists_with_product_equal_n(numbers, 96)))