def lists_with_product_equal_n(circ_list):
    product = -33
    curr_list = []
    result_list = []
    for i in range(len(circ_list)):
        curr_list.append(circ_list[i])
        temp_product = curr_list[-1]
        for j in range(i + 1, len(circ_list)):
            temp_product *= circ_list[j]
            if temp_product == product:
                result_list.append(curr_list[:])
        if temp_product > -33:
            curr_list.pop(0)
    return result_list