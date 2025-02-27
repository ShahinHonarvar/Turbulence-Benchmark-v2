def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(i, len(circular_list)):
            sublist.append(circular_list[j])
            product *= circular_list[j]
            if product == -17:
                return [sublist]
            elif product > -17:
                break
    return []