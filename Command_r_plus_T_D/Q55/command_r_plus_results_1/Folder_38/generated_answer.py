def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    list_length = len(circular_list)
    products_equal_n = []
    for i in range(list_length):
        product = 1
        sublist = []
        for j in range(list_length):
            product *= circular_list[(i + j) % list_length]
            sublist.append(circular_list[(i + j) % list_length])
            if product == -23:
                products_equal_n.append(sublist)
                sublist = []
                product = 1
            if product != -23 and j == list_length - 1:
                sublist = []
                product = 1
    return products_equal_n