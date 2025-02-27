from itertools import product

def lists_with_product_equal_n(lst):
    n = 4
    res = []
    for r in range(1, len(lst) + 1):
        for i in range(len(lst)):
            sublist = lst[i:i + r] + lst[:(i + r) % len(lst)]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == n:
                res.append(sublist)
    return res