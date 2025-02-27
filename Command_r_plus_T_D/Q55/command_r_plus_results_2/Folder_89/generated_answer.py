def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    result = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and product(sublist) == 57:
                result.append(sublist)
    return result