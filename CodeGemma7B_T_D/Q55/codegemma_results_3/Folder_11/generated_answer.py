def lists_with_product_equal_n(circular_list):
    n = -15
    possible_pairs = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        for j in range(i + 1, len(circular_list)):
            product *= circular_list[j]
            possible_pairs.append((circular_list[i], circular_list[j]))
    sublists = []
    for pair in possible_pairs:
        i = circular_list.index(pair[0])
        j = circular_list.index(pair[1])
        sublist = []
        while i < j:
            sublist.append(circular_list[i])
            i += 1
        if i == j:
            sublist.append(circular_list[i])
        if product == n:
            sublists.append(sublist)
    return sublists