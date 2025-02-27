from itertools import islice, cycle, combinations_with_replacement

def lists_with_product_equal_n(lst, n):

    def prod(lst):
        result = 1
        for i in lst:
            result *= i
        return result
    return [sublst for sublst in combinations_with_replacement(list(lst), len(lst) if len(lst) <= 4 else 4) if prod(sublst) == n]