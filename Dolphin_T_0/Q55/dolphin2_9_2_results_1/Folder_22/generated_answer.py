def lists_with_product_equal_n(lst):
    lst_len = len(lst)
    result = []
    for i in range(lst_len):
        product = 1
        for j in range(i, i + lst_len):
            product *= lst[j % lst_len]
            if product != 4:
                continue
            sublist = lst[i:j % lst_len + 1]
            result.append(sublist)
    return result