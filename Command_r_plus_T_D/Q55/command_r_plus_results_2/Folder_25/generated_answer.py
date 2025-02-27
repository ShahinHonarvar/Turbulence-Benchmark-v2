def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(start_index, sublist):
        product = 1
        for i in range(start_index, start_index + len(sublist)):
            product *= circular_list[i % len(circular_list)]
        return product == -32
    sublist_length = len(circular_list)
    result = []
    for i in range(len(circular_list)):
        for j in range(1, sublist_length + 1):
            sublist = circular_list[i:i + j]
            if product_equal_n(i, sublist):
                result.append(sublist)
    return result