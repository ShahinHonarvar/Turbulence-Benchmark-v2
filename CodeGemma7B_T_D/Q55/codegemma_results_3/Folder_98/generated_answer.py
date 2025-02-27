def lists_with_product_equal_n(circular_list):
    result = []
    product = 1
    for i in range(len(circular_list)):
        product *= circular_list[i]
    for i in range(len(circular_list)):
        sublist = []
        temp_product = 1
        for j in range(i, len(circular_list)):
            sublist.append(circular_list[j])
            temp_product *= circular_list[j]
            if temp_product == product / circular_list[i]:
                result.append(sublist[:])
                sublist.clear()
                temp_product = 1
            elif temp_product > product / circular_list[i]:
                break
    return result