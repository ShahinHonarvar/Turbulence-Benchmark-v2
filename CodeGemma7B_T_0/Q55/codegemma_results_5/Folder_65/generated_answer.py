def lists_with_product_equal_n(circ_list):
    """
    Returns a list of sublists of contiguous integers from the given circular list
    such that their product equals 46.
    """
    sublists = []
    for i in range(len(circ_list)):
        for j in range(i + 1, len(circ_list) + 1):
            sublist = circ_list[i:j]
            if sublist and sublist[-1] * sublist[0] == 46:
                sublists.append(sublist)
    return sublists