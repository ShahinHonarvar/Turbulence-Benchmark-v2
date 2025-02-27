from itertools import combinations

def lists_with_product_equal_n(lst):
    result = []
    for i in range(1, len(lst) + 1):
        for comb in combinations(lst, i):
            if 1 <= i <= len(lst) and -115 == comb.prod():
                result.append(list(comb))
    return result