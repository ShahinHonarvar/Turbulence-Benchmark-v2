def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    result = []
    product = 1
    for i in range(len(circular_list)):
        product *= circular_list[i]
        if product == 5:
            result.append(circular_list[i - len(circular_list) + 1:i + 1])
            product = 1
    return result