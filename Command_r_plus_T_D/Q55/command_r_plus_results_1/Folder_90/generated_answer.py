def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    list_length = len(circular_list)
    products_equal_n = []
    for i in range(list_length):
        product = 1
        sublist = []
        for j in range(i, list_length + i):
            sublist.append(circular_list[j % list_length])
            product *= circular_list[j % list_length]
            if product == -690:
                products_equal_n.append(sublist)
    return products_equal_n