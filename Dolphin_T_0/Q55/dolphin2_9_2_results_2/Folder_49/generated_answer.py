def lists_with_product_equal_n(lst, n=-61):
    if not lst:
        return []
    len_lst = len(lst)
    sublists = []
    for i in range(len_lst):
        product = 1
        for j in range(i, len_lst):
            product *= lst[j % len_lst]
            if product == n:
                sublists.append(lst[i:j + 1])
    return sublists