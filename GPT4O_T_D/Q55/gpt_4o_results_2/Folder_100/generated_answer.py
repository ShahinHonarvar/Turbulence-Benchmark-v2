from functools import reduce
from operator import mul

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length - 1) % n
            product *= circular_list[end]
            if length > 1 and end == start:
                break
            if product == 48:
                sublist = [circular_list[(start + i) % n] for i in range(length)]
                result.append(sublist)
            elif product == 0:
                break
    return result