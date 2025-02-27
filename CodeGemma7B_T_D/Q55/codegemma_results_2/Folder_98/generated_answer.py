def lists_with_product_equal_n(circular_list):
    product = 1
    sublists = []
    start_index = 0
    for i in range(len(circular_list)):
        product *= circular_list[i]
        while product == -1:
            sublists.append(circular_list[start_index:i + 1])
            product /= circular_list[start_index]
            start_index += 1
    return sublists