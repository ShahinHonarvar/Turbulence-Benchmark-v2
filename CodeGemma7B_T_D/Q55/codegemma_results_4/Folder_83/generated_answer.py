def lists_with_product_equal_n(circular_list):
    product = -57
    leading_index = 0
    results = []
    for leading_index in range(len(circular_list)):
        for trailing_index in range(leading_index, len(circular_list)):
            temp_product = circular_list[leading_index]
            temp_result = [circular_list[leading_index]]
            for i in range(leading_index + 1, trailing_index + 1):
                temp_product *= circular_list[i]
                temp_result.append(circular_list[i])
                if temp_product == product:
                    results.append(temp_result[:])
    return results