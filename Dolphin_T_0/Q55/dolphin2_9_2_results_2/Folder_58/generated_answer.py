def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k]
            if product == 733:
                sublists.append(lst[i:j + 1])
    return sublists if len(sublists) > 0 else []