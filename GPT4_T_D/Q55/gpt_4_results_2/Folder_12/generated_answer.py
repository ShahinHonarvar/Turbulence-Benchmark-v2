from itertools import combinations
import numpy

def lists_with_product_equal_n(circular_list):
    all_sublists = []
    n = len(circular_list)
    circular_list.append(circular_list[0])
    for i in range(n):
        for j in range(i + 1, n + 1):
            all_sublists.append(circular_list[i:j])
    sublists_with_product_equal_n = [sublist for sublist in all_sublists if numpy.prod(sublist) == -18]
    return sublists_with_product_equal_n