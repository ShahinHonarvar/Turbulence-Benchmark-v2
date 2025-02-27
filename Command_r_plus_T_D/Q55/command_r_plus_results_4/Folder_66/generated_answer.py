def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equals_seventy_eight(sublist: list[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == 78
    result = []
    list_length = len(circular_list)
    for start_index in range(list_length):
        for sublist_length in range(1, list_length + 1):
            end_index = (start_index + sublist_length) % list_length
            sublist = circular_list[start_index:end_index + 1]
            if product_equals_seventy_eight(sublist):
                result.append(sublist)
    return result