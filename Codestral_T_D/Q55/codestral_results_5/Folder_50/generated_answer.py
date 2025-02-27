from itertools import combinations
from functools import reduce
import operator

def lists_with_product_equal_n(circular_list):
    n = 45
    result = []
    list_len = len(circular_list)
    circular_list = circular_list + circular_list
    for i in range(list_len):
        for j in range(i + 1, i + list_len + 1):
            sub_list = circular_list[i:j]
            if reduce(operator.mul, sub_list, 1) == n:
                result.append(sub_list)
    return result