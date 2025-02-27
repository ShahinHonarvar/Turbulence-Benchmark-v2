from collections import deque

def lists_with_product_equal_n(lst):
    lst = deque(lst)
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, n):
            product *= lst[j]
            sublist.append(lst[j])
            if product == -18:
                result.append(sublist)
            if product == 0:
                break
        if lst[i] == 0:
            continue
        product = 1
        sublist = []
        for j in range(i - 1, -1, -1):
            product *= lst[j]
            sublist.append(lst[j])
            if product == -18:
                result.append(sublist)
            if product == 0:
                break
    return result