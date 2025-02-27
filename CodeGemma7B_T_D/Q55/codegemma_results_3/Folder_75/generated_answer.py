def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        product = circular_list[i]
        sublist = [circular_list[i]]
        j = (i + 1) % len(circular_list)
        while product == 13 and j != i:
            product *= circular_list[j]
            sublist.append(circular_list[j])
            j = (j + 1) % len(circular_list)
        if product == 13:
            result.append(sublist)
    return result