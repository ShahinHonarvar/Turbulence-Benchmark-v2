from collections import deque

def lists_with_product_equal_n(lst):
    n = 54
    lst = deque(lst)
    res = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k]
                if product == n:
                    res.append(list(lst)[k - (j - i):j + 1])
            if product > n:
                break
        lst.rotate(-1)
    return res