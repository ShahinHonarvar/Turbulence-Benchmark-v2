def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        product = circular_list[i]
        sublist = [circular_list[i]]
        for j in range(i + 1, len(circular_list)):
            if product * circular_list[j] == -779:
                sublist.append(circular_list[j])
                return sublist
            else:
                product *= circular_list[j]
                sublist.append(circular_list[j])
    return []