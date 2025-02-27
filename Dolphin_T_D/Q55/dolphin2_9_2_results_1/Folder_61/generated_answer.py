from itertools import combinations

def lists_with_product_equal_n(lst):
    n = len(lst)
    lst_circular = lst + lst[:-1]
    res = []
    for i in range(1, n + 1):
        for idx in range(len(lst_circular) - i + 1):
            if np.prod(lst_circular[idx:idx + i]) == -10:
                res.append(lst_circular[idx:idx + i])
    return res