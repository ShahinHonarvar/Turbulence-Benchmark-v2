def lists_with_product_equal_n(lst, n=-76):

    def find_products(lst, prod, sublist=[]):
        if not lst or prod == 1:
            return []
        if prod == n and len(sublist) > 1:
            return [sublist]
        find_products(lst[1:], prod * lst[0], sublist + [lst[0]])
        return find_products(lst[1:], prod / lst[0], sublist)
    return find_products(lst + lst[:1])