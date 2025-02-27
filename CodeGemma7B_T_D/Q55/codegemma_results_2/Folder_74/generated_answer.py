def lists_with_product_equal_n(circular_list):
    product = 51
    sublists = []
    for i in range(len(circular_list)):
        current_product = circular_list[i]
        current_sublist = [circular_list[i]]
        for j in range(i + 1, len(circular_list)):
            current_product *= circular_list[j % len(circular_list)]
            current_sublist.append(circular_list[j % len(circular_list)])
            if current_product == product:
                sublists.append(current_sublist[:])
        if current_product == product:
            sublists.append([circular_list[i]])
    return sublists