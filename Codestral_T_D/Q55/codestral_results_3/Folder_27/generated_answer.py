import numpy as np

def lists_with_product_equal_n(lst):
    n = -82
    res = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1]
            if len(sublist) <= len(lst) and np.prod(sublist) == n:
                res.append(sublist)
        if lst[i] == n:
            res.append([lst[i]])
    return res