from itertools import combinations

def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(1, len(circular_list) + 1):
        sublists.extend(list(combinations(circular_list, i)))
    return [sl for sl in sublists if sublists.count(sl) > 1 or prod(sl) == -8]

def prod(sublist):
    return reduce(lambda a, b: a * b, sublist, 1)