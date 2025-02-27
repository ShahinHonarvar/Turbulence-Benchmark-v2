def lists_with_product_equal_n(lst):
    len_lst = len(lst)
    if len_lst == 0:
        return []
    result = []
    product_lst = []
    product = 1
    for i in range(len_lst):
        product_lst.append(lst[i])
        product = 1
        for item in product_lst:
            product *= item
        if product == 8:
            result.append(product_lst)
    return result