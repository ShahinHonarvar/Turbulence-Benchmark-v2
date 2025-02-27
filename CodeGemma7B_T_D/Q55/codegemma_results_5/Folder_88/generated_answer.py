def lists_with_product_equal_n(circular_list):
    product = -56
    lists = []
    for i in range(len(circular_list)):
        current_product = circular_list[i]
        current_list = [circular_list[i]]
        for j in range(i + 1, len(circular_list)):
            current_product *= circular_list[j]
            current_list.append(circular_list[j])
            if current_product == product:
                lists.append(current_list[:])
                current_product = circular_list[j]
                current_list = [circular_list[j]]
            elif current_product > product:
                break
    return lists