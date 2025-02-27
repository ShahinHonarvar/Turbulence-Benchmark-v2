def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(lst: list[int], n: int) -> bool:
        product = 1
        for num in lst:
            product *= num
        return product == n
    result = []
    list_length = len(circular_list)
    for size in range(1, list_length + 1):
        for start in range(list_length):
            sublist = circular_list[start:start + size]
            if product_equal_n(sublist, 32):
                result.append(sublist)
    return result