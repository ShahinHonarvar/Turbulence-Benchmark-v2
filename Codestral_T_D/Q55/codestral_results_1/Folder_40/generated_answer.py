from collections import deque

def lists_with_product_equal_n(lst):
    n = len(lst)
    circular_lst = lst + lst[:-1]
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= circular_lst[j]
            if product == -9:
                result.append(circular_lst[i:j + 1])
    return result