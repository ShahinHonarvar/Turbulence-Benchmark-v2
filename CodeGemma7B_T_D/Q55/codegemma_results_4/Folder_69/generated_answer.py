def lists_with_product_equal_n(circ_list):
    for i in range(len(circ_list)):
        temp_list = [circ_list[i]]
        j = (i + 1) % len(circ_list)
        while temp_list[-1] * circ_list[j] == 90 and j != i:
            temp_list.append(circ_list[j])
            j = (j + 1) % len(circ_list)
        if len(temp_list) != 1 and temp_list not in result:
            result.append(temp_list)
    return result