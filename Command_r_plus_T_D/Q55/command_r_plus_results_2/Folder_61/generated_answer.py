def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(lst: list[int], n: int) -> bool:
        product = 1
        for num in lst:
            product *= num
        return product == n
    result = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if product_equal_n(sublist, -10):
                result.append(sublist)
    return result