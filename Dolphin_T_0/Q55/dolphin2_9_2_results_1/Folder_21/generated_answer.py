def lists_with_product_equal_n(lst):
    circ_lst = lst + lst[:1]
    sublst = []
    for i in range(len(circ_lst)):
        for j in range(i + 1, len(circ_lst)):
            prod = 1
            for k in range(i, j + 1):
                prod *= circ_lst[k]
            if prod == 851:
                sublst.append(circ_lst[i:j + 1])
    return sublst