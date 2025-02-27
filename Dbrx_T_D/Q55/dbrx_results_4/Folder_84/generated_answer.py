from itertools import combinations, islice

def lists_with_product_equal_n(numbers):

    def circular_sublists(numbers):
        for i in range(1, len(numbers) + 1):
            for j in combinations(range(len(numbers)), i):
                yield list(islice(numbers, i))[j]

    def has_product_equal_n(sublist, n):
        return any((x * n < 0 and abs(x * n) in set(sublist) for x in sublist))
    return [sublist for sublist in circular_sublists(numbers) if has_product_equal_n(sublist, -906)]