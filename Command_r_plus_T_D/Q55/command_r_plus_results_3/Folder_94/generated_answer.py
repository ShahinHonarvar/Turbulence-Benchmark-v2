def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    list_length = len(circular_list)
    products_equal_to_n = []
    for i in range(list_length):
        product = 1
        sublist = []
        for j in range(list_length):
            sublist.append(circular_list[(i + j) % list_length])
            product *= sublist[-1]
            if product == -30:
                products_equal_to_n.append(sublist)
                product = 1
                sublist = []
            elif product == 0:
                break
    return products_equal_to_n