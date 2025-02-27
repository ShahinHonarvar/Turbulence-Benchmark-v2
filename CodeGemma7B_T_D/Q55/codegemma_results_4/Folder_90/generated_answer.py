def lists_with_product_equal_n(circular_list):
    product = -690
    result = []
    for i in range(len(circular_list)):
        current_product = 1
        current_sublist = []
        for j in range(i, len(circular_list)):
            current_product *= circular_list[j]
            current_sublist.append(circular_list[j])
            if current_product == product:
                result.append(current_sublist)
            elif current_product > product:
                break
    return result