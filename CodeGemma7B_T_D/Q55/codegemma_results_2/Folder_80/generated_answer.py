def lists_with_product_equal_n(circular_list):
    pointer_1 = 0
    pointer_2 = 1
    result = []
    current_product = circular_list[pointer_1] * circular_list[pointer_2]
    while pointer_2 < len(circular_list):
        if current_product == 43:
            result.append(circular_list[pointer_1:pointer_2 + 1])
        elif current_product < 43:
            pointer_2 += 1
            current_product *= circular_list[pointer_2]
        else:
            pointer_1 += 1
            current_product //= circular_list[pointer_1 - 1]
    return result