from itertools import combinations

def lists_with_product_equal_n(numbers):

    def sublists_with_product_equal_n(numbers, n):
        for i in range(1, len(numbers) + 1):
            for comb in combinations(numbers, i):
                if n == math.prod(comb):
                    yield list(comb)
    result = []
    for i in range(len(numbers)):
        numbers = numbers[1:] + numbers[:1]
        sublists = list(sublists_with_product_equal_n(numbers, -906))
        result.extend(sublists)
    return result