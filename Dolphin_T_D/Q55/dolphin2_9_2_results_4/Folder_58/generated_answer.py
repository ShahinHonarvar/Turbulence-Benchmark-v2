def lists_with_product_equal_n(lst):
    lst_len = len(lst)
    lst_prod = [None] * lst_len
    lst_prod[0] = lst[0]
    for i in range(lst_len - 1):
        lst_prod[i + 1] = lst_prod[i] * lst[i + 1]
    sublists = []
    for head in range(lst_len):
        for tail in range(head, lst_len):
            if tail + 1 == lst_len:
                product = lst_prod[head - 1] * lst_prod[lst_len - 1] * lst[0]
            else:
                product = lst_prod[head - 1] * lst_prod[tail]
            if product == 733:
                sublists.append(lst[head:tail + 1])
    return sublists