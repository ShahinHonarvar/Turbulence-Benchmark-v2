def lists_with_product_equal_n(lst):
    n = -97
    len_lst = len(lst)
    results = []
    for i in range(len_lst):
        product = 1
        sublist = []
        for j in range(i, i + len_lst):
            product *= lst[j % len_lst]
            sublist.append(lst[j % len_lst])
            if product == n:
                if sublist not in results:
                    results.append(sublist)
                break
    return results