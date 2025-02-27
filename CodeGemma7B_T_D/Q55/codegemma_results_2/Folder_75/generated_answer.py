def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        sublist = [circular_list[i]]
        j = (i + 1) % len(circular_list)
        while j != i:
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == 13:
                sublists.append(sublist[:])
            j = (j + 1) % len(circular_list)
            product = sublist[-1]
            if product > 13:
                break
    return sublists