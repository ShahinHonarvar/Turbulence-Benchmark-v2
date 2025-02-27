from itertools import combinations
import numpy as np

def lists_with_product_equal_n(circular_list):
    result = []
    n = 93
    double_list = circular_list + circular_list
    for i in range(len(circular_list)):
        for j in range(i + 1, i + len(circular_list)):
            sublist = double_list[i:j]
            product = np.prod(sublist)
            if product == n:
                result.append(sublist)
    return result