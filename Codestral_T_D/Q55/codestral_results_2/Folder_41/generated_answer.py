from collections import deque

def lists_with_product_equal_n(lst):
    n = -20
    res = []
    for i in range(len(lst)):
        prod = 1
        sublst = deque()
        for j in range(i, len(lst) + i):
            prod *= lst[j % len(lst)]
            sublst.append(lst[j % len(lst)])
            while prod % n != 0 and sublst:
                prod /= sublst.popleft()
            if prod == n:
                res.append(list(sublst))
    return res