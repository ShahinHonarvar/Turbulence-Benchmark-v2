from itertools import combinations

def lists_with_product_equal_n(lst):
    n = -75
    result = []
    for r in range(1, len(lst) + 1):
        for i in range(len(lst)):
            for c in combinations(lst[i:] + lst[:i], r):
                if c not in result and prod(c) == n:
                    result.append(list(c))
    return result

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p