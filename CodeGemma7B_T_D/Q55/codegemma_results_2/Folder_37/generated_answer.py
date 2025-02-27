def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        sublist = []
        product = 1
        for j in range(i, len(circular_list)):
            sublist.append(circular_list[j])
            product *= circular_list[j]
            if product == -76:
                return sublist
            if product > -76:
                break
        for j in range(0, i):
            sublist.append(circular_list[j])
            product *= circular_list[j]
            if product == -76:
                return sublist
            if product > -76:
                break
    return []