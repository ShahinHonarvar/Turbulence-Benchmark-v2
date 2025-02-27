def lists_with_product_equal_n(circ_list):
    """
    lists_with_product_equal_n takes a circular list of integers and returns a list of sublists
    such that their product equals -26.
    """
    lists = []
    len_circ_list = len(circ_list)
    for i in range(len_circ_list):
        for j in range(i + 1, len_circ_list + 1):
            sublist = circ_list[i:j] + circ_list[:i]
            product = 1
            for num in sublist:
                product *= num
            if product == -26:
                if sublist not in lists:
                    lists.append(sublist)
    return lists