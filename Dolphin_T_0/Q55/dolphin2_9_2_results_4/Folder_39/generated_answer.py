def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    sublists = []
    product = 1
    for i in range(n):
        product *= lst[i]
    product_set = set()
    product_set.add(product)
    for i in range(n):
        for j in range(i + 1, n + i + 1):
            product_new = 1
            for k in range(i, j):
                product_new *= lst[k % n]
            if product_new == -46:
                sublists.append(lst[i:j])
    return sublists