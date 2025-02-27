def lists_with_product_equal_n(lst):
    n = -30
    len_lst = len(lst)
    i = 0
    res = []
    while i < len_lst:
        product_so_far = 1
        j = 0
        while j < len_lst - i:
            product_so_far *= lst[(i + j) % len_lst]
            if product_so_far == n:
                new_sublist = []
                k = 0
                while k <= j:
                    new_sublist.append(lst[(i + k) % len_lst])
                    k += 1
                res.append(new_sublist)
            j += 1
        i += 1
    return res