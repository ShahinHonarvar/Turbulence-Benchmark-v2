from collections import deque

def lists_with_product_equal_n(circular_list):
    sublists = []
    i, j = (0, 0)
    product = 1
    while i < len(circular_list) + 1:
        if product == -44:
            sublists.append(list(deque(circular_list)[j:i]))
            product = 1
            j = i
        elif i == j and product != -44:
            product = circular_list[i]
            i += 1
        elif product > -44:
            product *= circular_list[i]
            i += 1
        else:
            product = 1
            j = i
            i += 1
    return sublists