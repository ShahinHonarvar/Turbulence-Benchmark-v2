from collections import deque

def lists_with_product_equal_n(lst):
    n = 96
    circular_lst = deque(lst) * 2
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, i + len(lst)):
            product *= circular_lst[j]
            if product == n:
                result.append(list(circular_lst[i:j + 1]))
            elif product > n:
                break
    return result