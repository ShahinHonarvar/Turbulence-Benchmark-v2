def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_sublist_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if get_sublist_product(sublist) == -95:
                result.append(sublist)
    return result