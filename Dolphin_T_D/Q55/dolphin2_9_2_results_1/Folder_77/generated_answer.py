def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    products = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == 632:
                products.append(lst[i:j + 1])
    return products