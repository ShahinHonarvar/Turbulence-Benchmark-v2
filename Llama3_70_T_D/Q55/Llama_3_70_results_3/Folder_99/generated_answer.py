def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        current_list = []
        current_product = 1
        for j in range(len(circular_list)):
            index = (i + j) % len(circular_list)
            current_list.append(circular_list[index])
            current_product *= circular_list[index]
            if current_product == 415:
                result.append(current_list[:])
            elif current_product > 415:
                break
    return result