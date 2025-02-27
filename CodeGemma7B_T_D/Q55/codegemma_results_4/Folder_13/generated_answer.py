def lists_with_product_equal_n(circular_list):
    product = 54
    sublists = []
    for i in range(len(circular_list)):
        current_product = circular_list[i]
        current_sublist = [circular_list[i]]
        for j in range(i + 1, len(circular_list)):
            current_product *= circular_list[j]
            current_sublist.append(circular_list[j])
            if current_product == product:
                sublists.append(current_sublist.copy())
            if current_product > product:
                break
    return sublists