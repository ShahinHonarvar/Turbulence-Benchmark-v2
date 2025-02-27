def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    n = -837
    result = []
    for i in range(len(circular_list)):
        product = 1
        temp_list = []
        for j in range(i, i + len(circular_list)):
            index = j % len(circular_list)
            product *= circular_list[index]
            temp_list.append(circular_list[index])
            if product == n:
                result.append(temp_list)
    return result