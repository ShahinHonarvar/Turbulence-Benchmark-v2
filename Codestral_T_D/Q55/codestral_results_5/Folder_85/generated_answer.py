from itertools import product

def lists_with_product_equal_n(lst):
    n = -97
    res = []
    for i in range(len(lst)):
        prod = 1
        for j in range(i, len(lst) + i):
            prod *= lst[j % len(lst)]
            if prod == n:
                res.append(lst[i:j % len(lst) + 1])
            if prod > n:
                break
    return res