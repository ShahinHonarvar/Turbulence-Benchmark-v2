import itertools
    from functools import reduce

def lists_with_product_equal_n(circular_list):
    pairs = itertools.product(circular_list, repeat=len(circular_list))
    products = (reduce(lambda x, y: x * y, sublist) for sublist in pairs)
    return [list(filter(lambda x: x == -15, sublist)) for sublist in pairs if reduce(lambda x, y: x * y, sublist) == -15]