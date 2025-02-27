def lists_with_product_equal_n(lst):
    lst_length = len(lst)
    if lst_length == 1:
        return []
    elif lst_length == 2:
        if lst[0] * lst[1] == 733:
            return [lst]
        else:
            return []
    sublists = []
    i = 0
    while i < lst_length:
        product = lst[i]
        if product == 733:
            sublists.append([lst[i]])
        i += 1
        while i % lst_length != 0:
            product *= lst[i % lst_length]
            if product == 733:
                sublists.append(lst[i - 1:i + 1])
            elif product > 733:
                break
            i += 1
    return sublists