def lists_with_product_equal_n(lst):

    def get_sublist(lst, start, prod):
        sublists = []
        for i in range(start, len(lst)):
            sublists.extend(get_sublist(lst, i, prod * lst[i]))
            if prod * lst[i] == 45:
                sublists.append(lst[start:i + 1])
        return sublists
    sublists = get_sublist(lst, 0, 1)
    return sublists