from itertools import combinations

def lists_with_product_equal_n(numbers):
    result = []
    for i in range(1, len(numbers) + 1):
        for comb in combinations(numbers, i):
            if reduce(lambda x, y: x * y, comb) == -968:
                result.append(list(comb))
    return result