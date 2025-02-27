def lists_with_product_equal_n(circ_list):
    sublists = []
    current_product = 1
    current_sublist = []
    for i in range(len(circ_list)):
        current_product *= circ_list[i]
        current_sublist.append(circ_list[i])
        while current_product > -82:
            if current_product == -82:
                sublists.append(current_sublist[:])
            current_product //= circ_list[i]
            current_sublist.pop(0)
    return sublists