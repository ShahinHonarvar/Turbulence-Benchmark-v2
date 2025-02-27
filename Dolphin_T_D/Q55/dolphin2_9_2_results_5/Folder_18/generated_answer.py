def lists_with_product_equal_n(lst):
    n = len(lst)
    if n == 0:
        return []
    products = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product > 36:
                break
            if product == 36:
                products.append(lst[i:j + 1])
    return products