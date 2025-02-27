from collections import deque

def lists_with_product_equal_n(lst):
    lst = deque(lst)
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= lst[j % n]
            sublist.append(lst[j % n])
            if product == -41:
                result.append(sublist)
            if product == 0:
                break
    return result