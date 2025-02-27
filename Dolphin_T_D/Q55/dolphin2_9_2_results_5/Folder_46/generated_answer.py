def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            product = 1
            for k in range(i, j):
                product *= lst[k]
            if product == 53:
                sublists.append(lst[i:j])
    return sublists