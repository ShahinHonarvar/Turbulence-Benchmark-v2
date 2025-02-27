from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 18
    size = len(circular_list)
    circular_list += circular_list[:-1]
    result = []
    for start in range(size):
        product = 1
        for end in range(start, start + size):
            product *= circular_list[end % size]
            if product == n:
                result.append(circular_list[start:end % size + 1])
            elif product > n:
                break
    return result