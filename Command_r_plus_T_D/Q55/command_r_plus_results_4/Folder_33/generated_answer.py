def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    result = []
    product = -115
    size = len(circular_list)
    for i in range(size):
        temp_product = 1
        temp_list = []
        for j in range(i, size + i):
            temp_list.append(circular_list[j % size])
            temp_product *= circular_list[j % size]
            if temp_product == product:
                result.append(temp_list)
            if j == size + i - 1:
                temp_product = 1
                temp_list = []
    return result