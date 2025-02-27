def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(start_index, end_index):
        product = 1
        for i in range(start_index, end_index + 1):
            product *= circular_list[i % len(circular_list)]
        return product
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            if product_equal_n(i, j) == -8:
                result.append(circular_list[i:j + 1])
    return result