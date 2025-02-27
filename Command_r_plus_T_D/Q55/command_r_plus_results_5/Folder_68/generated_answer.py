def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    sublists = []
    product = 1
    for i in range(len(circular_list)):
        product *= circular_list[i]
        if product == 6:
            sublists.append(circular_list[:i + 1])
            product = 1
            circular_list = circular_list[i + 1:]
    return sublists