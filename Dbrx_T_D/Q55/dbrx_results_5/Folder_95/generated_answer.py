from itertools import combinations

def lists_with_product_equal_n(numbers):
    result = []
    n = 28
    for i in range(1, len(numbers) + 1):
        for comb in combinations(numbers, i):
            if comb not in result and isinstance(comb, tuple) and (reduce(lambda x, y: x * y, comb) == n):
                result.append(list(comb))
    return result