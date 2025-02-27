def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    products_equal_to_25 = []
    product_so_far = 1
    circular_list_length = len(circular_list)
    for i in range(circular_list_length):
        product_so_far = product_so_far * circular_list[i]
        if product_so_far == 25:
            products_equal_to_25.append(circular_list[:i + 1])
            product_so_far = 1
        if product_so_far == 1:
            product_so_far = circular_list[i]
    return products_equal_to_25