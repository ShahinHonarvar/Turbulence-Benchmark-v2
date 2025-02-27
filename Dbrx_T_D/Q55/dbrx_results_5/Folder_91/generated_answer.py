def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        subresult = []
        current_product = 1
        for j in range(i, len(circular_list)):
            current_product *= circular_list[j]
            subresult.append(circular_list[j])
            if current_product == 2:
                result.append(subresult.copy())
            elif current_product > 2:
                break
    return result