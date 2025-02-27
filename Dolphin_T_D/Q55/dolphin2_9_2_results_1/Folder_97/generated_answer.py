def lists_with_product_equal_n(lst):
    lst_len = len(lst)
    result = []
    for i in range(lst_len):
        product = lst[i]
        for j in range(i + 1, lst_len + 1):
            sublist = lst[i:j]
            if sublist[-1] < sublist[0]:
                product *= sublist[-1]
            else:
                product /= sublist[-1]
            if product == -938:
                result.append(sublist)
    return result