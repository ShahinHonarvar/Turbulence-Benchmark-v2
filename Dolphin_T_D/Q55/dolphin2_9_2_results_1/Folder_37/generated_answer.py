def lists_with_product_equal_n(input_list):
    product = -76
    length = len(input_list)
    result = []
    for sub_length in range(length, 0, -1):
        for start_point in range(length):
            if 1 == sub_length or input_list[start_point] * input_list[(start_point + 1) % length] == product:
                result.append(input_list[start_point:start_point + sub_length])
            elif sub_length > 2:
                current_product = 1
                for i in range(start_point, start_point + sub_length):
                    current_product *= input_list[i % length]
                if current_product == product:
                    result.append(input_list[start_point:start_point + sub_length])
    return result