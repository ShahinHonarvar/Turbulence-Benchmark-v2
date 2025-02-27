from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 78
    result = []
    circular_list = circular_list + circular_list
    for i in range(len(circular_list)):
        product = 1
        sublist = deque()
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == n:
                result.append(list(sublist))
            if product > n:
                break
    return result