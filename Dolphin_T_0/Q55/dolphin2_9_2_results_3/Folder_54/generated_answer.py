def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i > j:
                continue
            sublist_product = 1
            for k in range(i, j):
                sublist_product *= lst[k]
            if sublist_product == -17:
                sublists.append(lst[i:j])
    return sublists