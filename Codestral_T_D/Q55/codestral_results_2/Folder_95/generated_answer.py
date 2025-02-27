from collections import deque

def lists_with_product_equal_n(lst):
    n = 28
    lst *= 2
    res = []
    for i in range(len(lst)):
        pro = 1
        for j in range(i, len(lst)):
            pro *= lst[j]
            if pro == n:
                res.append(lst[i:j + 1])
            if pro > n:
                break
    return [sublist for sublist in res if len(sublist) <= len(lst) // 2]