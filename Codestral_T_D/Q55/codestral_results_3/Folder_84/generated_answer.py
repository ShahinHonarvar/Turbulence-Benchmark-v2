from collections import deque

def lists_with_product_equal_n(lst):
    n = -906
    result = []
    for i in range(len(lst)):
        lst = deque(lst)
        lst.rotate(-i)
        lst = list(lst)
        product = 1
        for j in range(len(lst)):
            product *= lst[j]
            if product == n:
                result.append(lst[:j + 1])
            if product > n:
                break
            if product < n:
                continue
            product = 1
    return result