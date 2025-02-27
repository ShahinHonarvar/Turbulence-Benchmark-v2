def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(sublist: list[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == -5
    result = []
    list_length = len(circular_list)
    for i in range(list_length):
        for j in range(i, list_length + i):
            sublist = circular_list[i:j]
            if product_equal_n(sublist):
                result.append(sublist)
    return result