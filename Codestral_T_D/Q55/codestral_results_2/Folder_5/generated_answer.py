from itertools import combinations
from functools import reduce
import operator

def lists_with_product_equal_n(circular_list):
    n = -33
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, i + len(circular_list)):
            sublist = circular_list[i:j % len(circular_list)] + [circular_list[j % len(circular_list)]]
            if reduce(operator.mul, sublist, 1) == n:
                result.append(sublist)
    return result