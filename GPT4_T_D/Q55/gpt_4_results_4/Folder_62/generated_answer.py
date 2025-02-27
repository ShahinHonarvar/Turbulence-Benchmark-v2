def lists_with_product_equal_n(circ_list):
    total_lists = []
    list_length = len(circ_list)
    circ_list = circ_list * 2
    for i in range(list_length):
        for j in range(i + 1, i + list_length + 1):
            sublist = circ_list[i:j]
            product = 1
            for item in sublist:
                product *= item
            if product == 100:
                total_lists.append(sublist)
    return total_lists