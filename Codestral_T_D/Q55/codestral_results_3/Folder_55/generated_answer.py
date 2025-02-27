from itertools import product

def lists_with_product_equal_n(lst):
    n = -6
    results = []
    for r in range(1, len(lst) + 1):
        for comb in product(range(len(lst)), repeat=r):
            sublist = [lst[i] for i in comb]
            if len(sublist) > 1 and len(sublist) <= len(lst) and (prod(sublist) == n):
                results.append(sublist)
    return results

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p