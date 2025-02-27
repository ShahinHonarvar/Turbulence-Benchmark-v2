def lists_with_product_equal_n(lst):

    def compute_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    if len(lst) == 0:
        return []
    product = compute_product(lst)
    if product == -97:
        return [lst]
    elif product != -1 and len(lst) != 1:
        return [lists_with_product_equal_n(lst[1:] + [lst[0]])]
    elif len(lst) == 1:
        return []
    else:
        return []