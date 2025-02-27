def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    target_product = -46
    list_size = len(circular_list)
    result = []
    for i in range(list_size):
        product = 1
        sublist = []
        for j in range(i, i + list_size):
            index = j % list_size
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == target_product:
                result.append(sublist)
    return result