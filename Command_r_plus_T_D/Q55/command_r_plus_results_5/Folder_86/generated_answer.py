def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    target_product = -779
    list_length = len(circular_list)
    result = []
    for i in range(list_length):
        product = 1
        temp_list = []
        for j in range(list_length):
            product *= circular_list[(i + j) % list_length]
            temp_list.append(circular_list[(i + j) % list_length])
            if product == target_product:
                result.append(temp_list)
                product = 1
                temp_list = []
    return result