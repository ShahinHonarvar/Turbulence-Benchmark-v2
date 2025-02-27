def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if prod(lst[i:j + 1]) == -115:
                res.append(lst[i:j + 1])
    return res

def prod(lst):
    p = 1
    for x in lst:
        p *= x
    return p