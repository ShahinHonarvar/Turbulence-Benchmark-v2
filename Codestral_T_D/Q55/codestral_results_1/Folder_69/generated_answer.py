from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 90
    size = len(circular_list)
    circular_list += circular_list
    result = []
    for i in range(size):
        for j in range(i + 1, size + i + 1):
            product = 1
            for k in range(i, j):
                product *= circular_list[k]
                if product > n:
                    break
            else:
                if product == n:
                    result.append(circular_list[i:j])
    return result