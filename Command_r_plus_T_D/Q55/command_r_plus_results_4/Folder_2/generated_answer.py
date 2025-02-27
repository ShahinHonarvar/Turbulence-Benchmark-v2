def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    list_length = len(circular_list)
    result = []
    for i in range(list_length):
        product = 1
        temp_sublist = []
        for j in range(list_length):
            product *= circular_list[(i + j) % list_length]
            temp_sublist.append(circular_list[(i + j) % list_length])
            if product == -968:
                result.append(temp_sublist)
                product = 1
                temp_sublist = []
    return result