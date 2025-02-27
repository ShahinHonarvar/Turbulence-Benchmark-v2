def lists_with_product_equal_n(lst):
    n = -72
    result = []
    lst_len = len(lst)
    lst = lst + lst
    for i in range(lst_len):
        product = 1
        sublist = []
        for j in range(i, i + lst_len):
            product *= lst[j]
            sublist.append(lst[j])
            if product == n:
                if sublist not in result:
                    result.append(sublist)
            if product > n:
                break
    return result