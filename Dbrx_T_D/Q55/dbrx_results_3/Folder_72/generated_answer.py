from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sublists = [lst[i:i + size] for size in range(1, len(lst) - i + 1)]
        for sublist in sublists:
            if reduce(lambda x, y: x * y, sublist, 1) == 10:
                result.append(sublist)
    return result

def reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        initializer = next(it)
    accum_value = initializer
    for x in it:
        accum_value = func(accum_value, x)
    return accum_value