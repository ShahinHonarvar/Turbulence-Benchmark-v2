from itertools import product

def lists_with_product_equal_n(lst):
    n = -1
    lst = lst + lst[:-1]
    result = []
    for r in range(1, len(lst)):
        for i in range(len(lst) - r + 1):
            if prod(lst[i:i + r]) == n:
                result.append(lst[i:i + r])
    return result

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p