def lists_with_product_equal_n(lst):
    sublists = []
    lst_length = len(lst)
    for i in range(lst_length):
        for j in range(i + 1, lst_length + 1):
            if i == j:
                product = lst[i]
            else:
                product = lst[i]
                for k in range(i + 1, j):
                    product *= lst[k]
            if product == -65:
                sublists.append(lst[i:j])
    return sublists