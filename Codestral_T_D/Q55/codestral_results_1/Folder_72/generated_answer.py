from itertools import combinations

def lists_with_product_equal_n(lst):
    lst *= 2
    n = len(lst) // 2
    res = []
    for i in range(n):
        for j in range(i + 1, i + n):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k]
                if product > 10:
                    break
                if product == 10:
                    res.append(lst[i:j + 1])
    return res