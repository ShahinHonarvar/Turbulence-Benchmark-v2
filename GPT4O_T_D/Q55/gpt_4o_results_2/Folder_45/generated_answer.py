def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    sublists = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= circular_list[(i + j) % n]
            if product == -5:
                sublists.append([circular_list[(i + k) % n] for k in range(j + 1)])
            if abs(product) > abs(-5) and product != 0:
                break
    return sublists