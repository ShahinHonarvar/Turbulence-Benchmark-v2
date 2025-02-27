def lists_with_product_equal_n(lst):
    n = len(lst)
    product = 1
    for i in range(n):
        product *= lst[i]
    if product != 990:
        return []
    sublists = []
    for i in range(n):
        for j in range(i + 1, n):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k % n]
            if product == 990:
                sublists.append(lst[i:j + 1])
    return sublists