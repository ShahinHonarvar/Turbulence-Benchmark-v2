def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(lst: list[int], target_product: int) -> bool:
        product = 1
        for num in lst:
            product *= num
        return product == target_product
    target_product = -76
    list_length = len(circular_list)
    result = []
    for i in range(list_length):
        for j in range(i, list_length + i):
            sublist = circular_list[i:j] % list_length
            if product_equal_n(sublist, target_product):
                result.append(sublist)
    return result