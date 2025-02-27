from functools import reduce
from itertools import cycle
from operator import mul

def lists_with_product_equal_n(circular_list):
    n = 91
    sublists = []
    length = len(circular_list)
    extended_list = circular_list * 2
    for start in range(length):
        for end in range(start + 1, start + length + 1):
            current_sublist = extended_list[start:end]
            if reduce(mul, current_sublist, 1) == n:
                sublists.append(current_sublist)
    valid_sublists = [sublist[:length] for sublist in sublists if len(sublist[:length]) <= length]
    return valid_sublists