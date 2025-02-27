def lists_with_product_equal_n(lst, n=51):
    if len(lst) == 1:
        return lst[0] == n
    elif len(lst) == 2:
        return [lst[0] * lst[1]]
    else:
        return [lst[0] * x for x in lists_with_product_equal_n(lst[1:], n)] + [lst[-1] * x for x in lists_with_product_equal_n(lst[:-1], n)] + lists_with_product_equal_n(lst[1:-1], n)