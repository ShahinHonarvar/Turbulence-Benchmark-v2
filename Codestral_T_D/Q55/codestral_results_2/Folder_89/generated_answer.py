from collections import deque

def lists_with_product_equal_n(lst):
    lst = deque(lst)
    n = 57
    result = []
    for _ in range(len(lst)):
        product = 1
        sublist = []
        for i in range(len(lst)):
            product *= lst[i]
            sublist.append(lst[i])
            if product == n:
                result.append(sublist)
        lst.rotate(-1)
    return result