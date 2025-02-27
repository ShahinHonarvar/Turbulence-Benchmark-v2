def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        current_list = []
        for j in range(i, len(circular_list)):
            current_list.append(circular_list[j])
            product *= circular_list[j]
            if product == -5:
                result.append(current_list[:])
            if product > -5:
                break
        for j in range(0, i):
            current_list.append(circular_list[j])
            product *= circular_list[j]
            if product == -5:
                result.append(current_list[:])
            if product > -5:
                break
    return result