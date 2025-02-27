from itertools import islice, cycle, combinations

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        if not lst:
            return []
        sublists = [lst[i:j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1)]
        return [sublist for sublist in sublists if reduce(lambda x, y: x * y, sublist, 1) == n]
    result = sublists_with_product_equal_n(lst, 78)
    result.extend(flatten([[sublist[i:] + sublist[:i] for i in range(1, len(sublist))] for sublist in result]))
    result = list(set(map(tuple, result)))
    return result

def flatten(lst):
    return [item for sublist in lst for item in sublist]

def circular(lst):
    return tuple(islice(cycle(lst), 0, len(lst)))

def reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        initializer = next(it, None)
    accum_value = initializer
    for x in it:
        accum_value = func(accum_value, x)
    return accum_value