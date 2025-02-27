from collections import deque

def lists_with_product_equal_n(lst):
    n = -69
    circular_lst = deque(lst + lst)
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, i + len(lst)):
            product *= circular_lst[j]
            sublist.append(circular_lst[j])
            if product == n:
                result.append(sublist)
    return result