def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, i + len(circular_list)):
            index = j % len(circular_list)
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == -16:
                result.append(sublist)
                sublist = []
                product = 1
    return result