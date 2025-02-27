def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    products_equal_to_99 = []
    for i in range(len(circular_list)):
        product = 1
        temp_sublist = []
        for j in range(i, i + len(circular_list)):
            index = j % len(circular_list)
            product *= circular_list[index]
            temp_sublist.append(circular_list[index])
            if product == 99:
                products_equal_to_99.append(temp_sublist)
                product = 1
                temp_sublist = []
    return products_equal_to_99