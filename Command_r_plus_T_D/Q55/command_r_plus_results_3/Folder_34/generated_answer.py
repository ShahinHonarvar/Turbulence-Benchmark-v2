def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product
    result = []
    list_length = len(circular_list)
    for length in range(1, list_length + 1):
        for start_index in range(list_length):
            sublist = circular_list[start_index:start_index + length]
            if get_product(sublist) == -81:
                result.append(sublist)
    return result