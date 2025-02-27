def lists_with_product_equal_n(lst):
    if not lst:
        return []
    product = -23
    sublist_prod = [1]
    for i in range(1, len(lst) + 1):
        sublist_prod.append(sublist_prod[-1] * lst[i - 1])
    result = []
    lst_len = len(lst)
    for length in range(1, lst_len + 1):
        sublist = []
        for i in range(lst_len):
            if sublist_prod[i] == product and sublist_prod[i + length] / sublist_prod[i] == product:
                sublist.append(lst[i:i + length])
        if sublist:
            result.extend(sublist)
    return result