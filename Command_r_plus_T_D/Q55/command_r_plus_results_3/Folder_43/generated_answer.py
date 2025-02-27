def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product
    result = []
    list_length = len(circular_list)
    for i in range(list_length):
        for j in range(i, i + list_length):
            sublist = circular_list[i:j] % list_length
            if get_product(sublist) == -26:
                result.append(sublist)
    return result