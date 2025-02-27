def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    list_length = len(circular_list)
    products_equal_to_n = []
    for i in range(list_length):
        product = 1
        sublist = []
        for j in range(i, list_length + i):
            sublist.append(circular_list[j % list_length])
            product *= sublist[-1]
            if product == -1:
                products_equal_to_n.append(sublist)
            if product != -1 and j - i + 1 == list_length:
                break
    return products_equal_to_n