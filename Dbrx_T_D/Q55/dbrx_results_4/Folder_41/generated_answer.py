from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = -20
    result = []
    for i in range(1, len(circular_list) + 1):
        for comb in combinations(circular_list, i):
            if reduce(lambda x, y: x * y, comb, 1) == n:
                result.append(list(comb))
    return result