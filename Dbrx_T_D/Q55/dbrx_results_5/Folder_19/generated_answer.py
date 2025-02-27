from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = -54
    sublists = []
    for i in range(len(circular_list)):
        window_sublists = [list(islice(cycle(circular_list), i, i + j + 1)) for j in range(len(circular_list))]
        products = [prod(sublist) for sublist in window_sublists]
        sublists.extend([sublist for sublist, product in zip(window_sublists, products) if product == n])
    return sublists

def prod(iterable):
    return functools.reduce(lambda x, y: x * y, iterable, 1)