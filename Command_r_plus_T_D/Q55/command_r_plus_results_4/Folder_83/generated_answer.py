def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    target_product = -57
    list_length = len(circular_list)
    result = []
    for i in range(list_length):
        product = 1
        sublist = []
        for j in range(list_length):
            product *= circular_list[(i + j) % list_length]
            sublist.append(circular_list[(i + j) % list_length])
            if product == target_product:
                result.append(sublist)
                product = 1
                sublist = []
    return result