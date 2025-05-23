def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    products_equal_to_15 = []
    product_so_far = 1
    for i in range(len(circular_list)):
        product_so_far = product_so_far * circular_list[i]
        if product_so_far == 15:
            products_equal_to_15.append(circular_list[i - 3:i + 1])
        if product_so_far == 15 and circular_list[i] == 1:
            products_equal_to_15.append(circular_list[i:i + 4])
    return products_equal_to_15