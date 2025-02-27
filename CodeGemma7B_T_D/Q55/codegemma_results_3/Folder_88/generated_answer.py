def lists_with_product_equal_n(circular_list):
    product = -56
    result = []
    for i in range(len(circular_list)):
        current_product = 1
        temp_list = []
        for j in range(i, len(circular_list)):
            current_product *= circular_list[j]
            temp_list.append(circular_list[j])
            if current_product == product:
                if temp_list not in result:
                    result.append(temp_list)
            if current_product > product:
                break
    return result