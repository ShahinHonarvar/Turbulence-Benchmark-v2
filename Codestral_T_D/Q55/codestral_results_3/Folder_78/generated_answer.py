from collections import deque

def lists_with_product_equal_n(lst):
    lst = deque(lst)
    n = len(lst)
    res = []
    for i in range(n):
        prod = 1
        sublst = []
        for j in range(i, i + n):
            prod *= lst[j % n]
            sublst.append(lst[j % n])
            if prod == 74:
                res.append(sublst)
            if prod >= 74:
                while prod >= 74 and i < j:
                    prod /= lst[i]
                    i += 1
                    if i < j and prod == 74:
                        res.append(sublst[i:j + 1])
    return res