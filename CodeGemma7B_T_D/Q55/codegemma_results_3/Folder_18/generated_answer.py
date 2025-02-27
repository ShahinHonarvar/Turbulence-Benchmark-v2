def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        product = circular_list[i]
        sublist = [circular_list[i]]
        for j in range(i + 1, len(circular_list)):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == 36 and len(sublist) <= len(circular_list):
                result.append(sublist[:])
        circular_list.append(circular_list.pop(0))
    return result