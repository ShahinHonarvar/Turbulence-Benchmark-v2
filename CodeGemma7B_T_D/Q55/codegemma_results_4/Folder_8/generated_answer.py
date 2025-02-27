from itertools import chain, combinations

@circular_list_access
def lists_with_product_equal_n(lst):
    return [list(g) for _, g in groupby(sorted(lst * 2), partial(operator.mul, n))]