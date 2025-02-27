def lists_with_product_equal_n(lst):
    n = len(lst)
    product = -72
    sublists = []
    for length in range(1, n + 1):
        for i in range(n):
            product_sublist = 1
            sub_lst = []
            for j in range(i, i + length):
                sub_lst.append(lst[j % n])
                product_sublist *= lst[j % n]
            if product_sublist == product:
                sublists.append(sub_lst)
    return sublists