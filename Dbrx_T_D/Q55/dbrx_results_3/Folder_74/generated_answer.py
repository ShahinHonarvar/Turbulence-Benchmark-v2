from itertools import combinations

def lists_with_product_equal_n(lst):
    res = []
    for i in range(1, len(lst) + 1):
        for j in combinations(lst, i):
            if j[0] * j[1:] == 51:
                res.append(list(j))
    return res