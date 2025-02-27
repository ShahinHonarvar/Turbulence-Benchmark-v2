def lists_with_product_equal_n(lst):
    n = 16
    products = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k % len(lst)]
                if product == -n:
                    products.append(lst[i:k + 1])
    return products