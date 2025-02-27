from itertools import combinations

def lists_with_product_equal_n(lst):
    lst *= 2
    n = 8
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if i < j - len(lst) // 2:
                product = 1
                for k in range(i, j):
                    product *= lst[k]
                    if product > n:
                        break
                    if product == n:
                        res.append(lst[i:j])
    return res