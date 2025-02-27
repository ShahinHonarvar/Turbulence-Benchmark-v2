def lists_with_product_equal_n(circular_list):
    cur_product = circular_list[0]
    for i in range(1, len(circular_list)):
        cur_product *= circular_list[i]
    result = []
    i = 0
    while i < len(circular_list):
        j = i + 1
        while j < len(circular_list):
            if cur_product / circular_list[i] / circular_list[j] == circular_list[(j + 1) % len(circular_list)]:
                temp_list = []
                temp_product = cur_product
                temp_j = j
                while temp_product / circular_list[(temp_j + 1) % len(circular_list)] == circular_list[(temp_j + 2) % len(circular_list)]:
                    temp_list.append(circular_list[temp_j + 1])
                    temp_product /= circular_list[temp_j + 1]
                    temp_j += 1
                temp_list.append(circular_list[temp_j])
                temp_list.append(circular_list[i])
                result.append(temp_list)
                break
            j += 1
        if temp_list:
            break
        i += 1
    return result