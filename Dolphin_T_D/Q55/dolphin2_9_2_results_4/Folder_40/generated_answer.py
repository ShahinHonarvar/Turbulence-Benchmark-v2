def lists_with_product_equal_n(lst, n=-9):

    def get_sublists(lst, product=1):
        if not lst:
            return []
        elif product == n:
            return [[]]
        elif product > n:
            return []
        else:
            return get_sublists(lst[:-1], product * lst[-1]) + get_sublists(lst[:-1], product)
    result = get_sublists(lst)
    result.extend(get_sublists(lst[::-1]))
    return result