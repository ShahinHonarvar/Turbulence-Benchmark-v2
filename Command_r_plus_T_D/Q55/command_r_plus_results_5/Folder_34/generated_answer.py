def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    list_length = len(circular_list)
    product_equal_n = []
    for i in range(list_length):
        product = 1
        sublist = []
        for j in range(list_length):
            product *= circular_list[(i + j) % list_length]
            sublist.append(circular_list[(i + j) % list_length])
            if product == -81:
                product_equal_n.append(sublist)
                sublist = []
                product = 1
    return product_equal_n