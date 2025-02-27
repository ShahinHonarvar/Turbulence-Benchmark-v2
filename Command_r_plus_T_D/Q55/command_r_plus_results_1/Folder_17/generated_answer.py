def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    products_equal_to_n = []
    product_so_far = 1
    for i in range(len(circular_list)):
        product_so_far *= circular_list[i]
        if product_so_far == 18:
            products_equal_to_n.append(circular_list[:i + 1])
            product_so_far = 1
            circular_list = circular_list[i + 1:]
    return products_equal_to_n