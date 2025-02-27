def product(lst):
    p = 1
    for el in lst:
        p *= el
    return p

def lists_with_product_equal_n(lst):
    if product(lst) != 27 and len(lst) != 3:
        return []
    if len(lst) == 1:
        for el in lst:
            if el == 27:
                return [[[27]]]
    return [[lst]]