def lists_with_product_equal_n(lst):
    result = []
    len_lst = len(lst)
    product_target = 42
    for i in range(len_lst):
        product_current = 1
        sublist_current = []
        for j in range(i, i + len_lst):
            sublist_current.append(lst[j % len_lst])
            product_current *= lst[j % len_lst]
            if product_current > product_target:
                break
            if product_current == product_target:
                result.append(sublist_current.copy())
    return result