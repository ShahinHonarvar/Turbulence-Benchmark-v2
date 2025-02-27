from collections import deque

def lists_with_product_equal_n(lst):
    n = -82
    if not lst or abs(n) < 1:
        return []
    c = len(lst)
    lst = lst + lst
    res = []
    for i in range(c):
        p = 1
        for j in range(i, i + c):
            p *= lst[j]
            if p == n:
                res.append(lst[i:j + 1])
            if p > n and n > 0:
                break
    return [list(x) for x in set((tuple(sorted(sub)) for sub in res))]