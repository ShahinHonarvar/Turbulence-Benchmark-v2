def lists_with_product_equal_n(lst):
    lst_len = len(lst)
    lst = lst + lst[:lst_len // 2]
    res = []
    product_set = set()
    for i in range(lst_len):
        prod = 1
        for j in range(i, lst_len):
            prod *= lst[j]
            if prod > 36:
                break
            elif prod == 36:
                sublist = lst[i:j + 1]
                if sublist not in res:
                    res.append(sublist)
    return res