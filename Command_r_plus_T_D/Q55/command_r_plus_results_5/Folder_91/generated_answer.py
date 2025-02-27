def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def is_product_equal_to_2(sublist: list[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == 2
    result = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if is_product_equal_to_2(sublist):
                result.append(sublist)
    return result