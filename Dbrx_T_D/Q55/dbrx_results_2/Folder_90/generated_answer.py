from itertools import islice, combinations, product
from more_itertools import circular_shifts

def lists_with_product_equal_n(circular_list):

    def sublist_with_product_equal_n(sublist):
        return reduce(lambda x, y: x * y, sublist) == -690
    shifts = circular_shifts(circular_list)
    sublists = (list(x) for x in combinations(shifts, len(shifts) // 2))
    sublists_with_product = filter(sublist_with_product_equal_n, sublists)
    return list(sublists_with_product)