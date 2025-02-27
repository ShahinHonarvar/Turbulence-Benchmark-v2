def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    prod_n = -76
    sublists = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == prod_n and [lst[j % n] for j in range(i, i + n)] not in sublists:
                sublists.append([lst[j % n] for j in range(i, i + n)])
    return sublists