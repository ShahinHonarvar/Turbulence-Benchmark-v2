from functools import reduce
from itertools import islice

def lists_with_product_equal_n(circular_list):

    def product(lst):
        return reduce(lambda x, y: x * y, lst, 1)
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = list(islice(circular_list, start, start + length))
            if len(sublist) < length:
                sublist.extend(circular_list[:length - len(sublist)])
            if product(sublist) == -72:
                result.append(sublist)
    return result