def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        product = circular_list[i]
        sublist = [circular_list[i]]
        for j in range(i + 1, len(circular_list)):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == -54:
                return sublist
            elif product > -54:
                break
    return []