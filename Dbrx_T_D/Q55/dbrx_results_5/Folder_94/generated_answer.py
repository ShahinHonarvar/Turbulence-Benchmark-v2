from itertools import combinations

def lists_with_product_equal_n(numbers):
    result = []
    n = -30
    for i in range(1, len(numbers) + 1):
        for comb in combinations(numbers, i):
            if i == 1 and comb[0] != n:
                continue
            if i > 1 and i <= len(numbers) // 2:
                prod = 1
                for j in comb:
                    prod *= j
                if prod == n:
                    result.append(list(comb))
    return result