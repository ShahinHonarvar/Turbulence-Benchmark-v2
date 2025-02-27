def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        current_list = [circular_list[i]]
        j = (i + 1) % len(circular_list)
        while product * circular_list[j] == -7 and j != i:
            product *= circular_list[j]
            current_list.append(circular_list[j])
            j = (j + 1) % len(circular_list)
        if product == -7:
            sublists.append(current_list)
    return sublists