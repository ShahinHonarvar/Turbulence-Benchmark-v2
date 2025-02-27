def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        sublist = [circular_list[i]]
        for j in range(i + 1, len(circular_list)):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == 29:
                sublists.append(sublist[:])
            elif product > 29:
                break
    return sublists