from itertools import combinations

def lists_with_product_equal_n(lst):
    n = len(lst)
    lst += lst
    res = []
    for i in range(n):
        for j in range(i + 1, i + n):
            sublst = lst[i:j]
            if len(sublst) > n:
                break
            if prod(sublst) == 33:
                res.append(sublst)
    return res

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p