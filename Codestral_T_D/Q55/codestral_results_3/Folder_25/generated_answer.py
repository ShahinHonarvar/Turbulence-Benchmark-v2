from itertools import cycle, islice
from functools import reduce
from operator import mul

def lists_with_product_equal_n(circ_list):
    n = -32
    result = []
    for i in range(len(circ_list)):
        for j in range(i + 1, i + len(circ_list)):
            sublist = list(islice(cycle(circ_list), i, j))
            if reduce(mul, sublist, 1) == n:
                result.append(sublist)
    return result