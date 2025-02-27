from collections import deque

def lists_with_product_equal_n(lst):
    n = -57
    result = []
    circular_lst = lst + lst
    for i in range(len(lst)):
        product = 1
        sublist = deque()
        for j in range(i, len(circular_lst)):
            sublist.append(circular_lst[j])
            product *= circular_lst[j]
            if product == n:
                result.append(list(sublist))
            elif product > n:
                break
    return result