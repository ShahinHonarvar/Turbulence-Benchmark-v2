from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 18
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, i + len(circular_list)):
            product *= circular_list[j % len(circular_list)]
            if product == n:
                result.append(circular_list[i:j % len(circular_list) + 1])
            if product > n:
                break
    return result