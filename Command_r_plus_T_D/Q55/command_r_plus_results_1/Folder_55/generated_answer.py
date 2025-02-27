def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    products_equal_n = []
    product = 1
    for i in range(len(circular_list)):
        product *= circular_list[i]
        if product == -6:
            products_equal_n.append(circular_list[:i + 1])
            product = 1
        if product == 0:
            product = 1
    return products_equal_n