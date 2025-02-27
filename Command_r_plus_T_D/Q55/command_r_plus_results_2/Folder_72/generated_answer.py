def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    target_product = 10
    list_length = len(circular_list)
    result = []
    for i in range(list_length):
        product = 1
        sublist = []
        for j in range(i, i + list_length):
            index = j % list_length
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == target_product:
                result.append(sublist)
                product = 1
                sublist = []
    return result