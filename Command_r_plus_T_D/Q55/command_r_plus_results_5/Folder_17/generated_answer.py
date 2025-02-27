def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    products_equal_to_18 = []
    list_length = len(circular_list)
    for i in range(list_length):
        product = 1
        sublist = []
        for j in range(list_length):
            sublist.append(circular_list[(i + j) % list_length])
            product *= sublist[-1]
            if product == 18:
                products_equal_to_18.append(sublist[:])
                sublist.clear()
                product = 1
    return products_equal_to_18