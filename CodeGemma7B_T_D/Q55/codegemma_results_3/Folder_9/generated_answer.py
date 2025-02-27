def lists_with_product_equal_n(circular_list):
    sublists = []
    product = -36
    for i in range(len(circular_list)):
        temp_product = circular_list[i]
        temp_sublist = [circular_list[i]]
        for j in range(i + 1, len(circular_list)):
            temp_product *= circular_list[j]
            temp_sublist.append(circular_list[j])
            if temp_product == product and len(temp_sublist) <= len(circular_list):
                sublists.append(temp_sublist)
        if temp_product == product and len(temp_sublist) <= len(circular_list):
            sublists.append(temp_sublist)
    return sublists