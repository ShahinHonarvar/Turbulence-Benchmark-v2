from functools import reduce
from operator import mul

def lists_with_product_equal_n(circular_list):

    def product(sublist):
        return reduce(mul, sublist, 1)
    result = []
    length = len(circular_list)
    for start in range(length):
        for size in range(1, length + 1):
            sublist = [circular_list[(start + i) % length] for i in range(size)]
            if product(sublist) == -54:
                result.append(sublist)
    return result