from itertools import combinations

def lists_with_product_equal_n(lst):
    n = -87
    res = []
    for r in range(1, len(lst) + 1):
        for i in range(len(lst)):
            for c in combinations(lst[i:] + lst[:i], r):
                if product(c) == n:
                    res.append(list(c))
    return res

def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p