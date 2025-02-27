def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    list_length = len(circular_list)
    products_equal_n = []
    for i in range(list_length):
        product = 1
        temp_sublist = [circular_list[i]]
        for j in range(1, list_length):
            product *= circular_list[(i + j) % list_length]
            temp_sublist.append(circular_list[(i + j) % list_length])
            if product == -6:
                products_equal_n.append(temp_sublist[:])
            if product != -6 and len(temp_sublist) == list_length:
                break
    return products_equal_n