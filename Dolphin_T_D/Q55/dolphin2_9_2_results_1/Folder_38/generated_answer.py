def lists_with_product_equal_n(lst):
    lst_len = len(lst)
    if lst_len == 0:
        return []
    prod_dict = {}
    for sublist_length in range(1, lst_len + 1):
        for i in range(lst_len):
            sublist = lst[i:i + sublist_length]
            sublist_product = 1
            for num in sublist:
                sublist_product *= num
            if sublist_product == -23 and sublist not in prod_dict.values():
                prod_dict[tuple(sublist)[0] * sublist_product] = sublist
    return list(prod_dict.values())