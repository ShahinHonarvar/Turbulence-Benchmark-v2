import itertools
from math import prod

def lists_with_product_equal_n(circ_list):
    circ_list *= 2
    result = []
    for i in range(len(circ_list) // 2):
        for j in range(i + 1, i + len(circ_list) // 2):
            sublist = circ_list[i:j]
            if prod(sublist) == -23:
                result.append(sublist)
    return result