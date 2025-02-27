def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def is_product_equal_to_n(sublist: list[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == 4
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j]
            if is_product_equal_to_n(sublist):
                result.append(sublist)
    return result