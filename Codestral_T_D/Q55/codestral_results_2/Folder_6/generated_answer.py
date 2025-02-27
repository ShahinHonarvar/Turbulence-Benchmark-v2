from collections import deque

def lists_with_product_equal_n(circular_list):
    n = 42
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list) + i):
            product *= circular_list[j % len(circular_list)]
            if product == n:
                result.append(circular_list[i:j % len(circular_list) + 1])
            elif product > n:
                break
            if product < 1:
                while product < 1 and i < j % len(circular_list):
                    product /= circular_list[i]
                    i += 1
                    if product == n:
                        result.append(circular_list[i:j % len(circular_list) + 1])
    return result