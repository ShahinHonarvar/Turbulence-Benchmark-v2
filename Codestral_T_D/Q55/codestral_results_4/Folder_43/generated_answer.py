from itertools import combinations
from functools import reduce
import operator

def lists_with_product_equal_n(circ_list):
    sublists = []
    for r in range(1, len(circ_list) + 1):
        for i in range(len(circ_list)):
            sublist = circ_list[i:i + r] + circ_list[:i]
            if reduce(operator.mul, sublist, 1) == -26:
                sublists.append(sublist)
    return sublists