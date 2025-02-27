def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        temp_list = []
        product = 1
        for j in range(i, len(circular_list)):
            temp_list.append(circular_list[j])
            product *= circular_list[j]
            if product == 49:
                result.append(temp_list)
            elif product > 49:
                break
        for j in range(0, i):
            temp_list.append(circular_list[j])
            product *= circular_list[j]
            if product == 49:
                result.append(temp_list)
            elif product > 49:
                break
    return result