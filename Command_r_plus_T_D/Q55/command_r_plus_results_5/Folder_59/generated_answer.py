def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    result = []
    product = -3
    length = len(circular_list)
    for i in range(length):
        curr_product = 1
        temp_list = []
        for j in range(i, i + length):
            index = j % length
            curr_product *= circular_list[index]
            temp_list.append(circular_list[index])
            if curr_product == product:
                result.append(temp_list)
                curr_product = 1
                temp_list = []
    return result