def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(sublist: list[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == 54
    length = len(circular_list)
    result = []
    for i in range(length):
        for j in range(i, length + i):
            sublist = circular_list[i:j] % length
            if product_equal_n(sublist):
                result.append(sublist)
    return result