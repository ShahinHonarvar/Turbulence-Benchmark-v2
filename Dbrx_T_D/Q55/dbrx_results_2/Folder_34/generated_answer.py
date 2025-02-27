from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists_with_product_equal_n(lst, n):
        for i in range(1, len(lst) + 1):
            sublists = (list(x) for x in itertools.combinations(lst, i))
            for sublist in sublists:
                if prod(sublist) == n:
                    yield sublist

    def prod(lst):
        return functools.reduce(lambda x, y: x * y, lst, 1)
    return list(set(sublists_with_product_equal_n(lst + lst, -81)) - set(sublists_with_product_equal_n(lst, -81)))

def circular_sublists_with_n_product(lst, n):
    return [sublist for sublist in sublists_with_product_equal_n(lst, n) if sublist and (sublist[0] == lst[0] or sublist[-1] == lst[-1])]

def lists_with_product_equal_n_circular(lst):
    if not lst:
        return []
    result = circular_sublists_with_n_product(lst[1:] + [lst[0]], -81)
    for sublist in result:
        if all((x != sublist[0] for x in lst)):
            result.remove(sublist)
    return result