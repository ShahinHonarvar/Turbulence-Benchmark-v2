def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    list_length = len(circular_list)
    product_list = []
    for i in range(list_length):
        product = 1
        temp_list = []
        for j in range(list_length):
            product *= circular_list[(i + j) % list_length]
            temp_list.append(circular_list[(i + j) % list_length])
            if product == -41:
                product_list.append(temp_list)
    return product_list