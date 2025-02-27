def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    products = {1: []}
    for i in range(n):
        product = 1
        for j in range(i, n * 2):
            product *= lst[j % n]
            if product == 43 and j - i + 1 > len(products[product]):
                products[product] = lst[i:(i + j - i + 1) % n]
    return list(products.values())