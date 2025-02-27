from itertools import combinations_with_replacement as cwr

def lists_with_product_equal_n(circlist, n):
    """Generates sublists with product equal to n in a circular list."""

    def is_sublist_ok(sublist):
        product = 1
        for element in sublist:
            product *= element
            if product > n:
                return False
        return product == n
    return [comb for comb in cwr(circlist) if is_sublist_ok(comb)]