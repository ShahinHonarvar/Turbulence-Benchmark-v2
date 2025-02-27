def lists_with_product_equal_n(circ_list):
    """
    This function takes a circular list of integers and returns a list of sublists each of which contains the contiguous integers from the given list such that their product equals -30.
    """
    sublists = []
    for i in range(len(circ_list)):
        for j in range(i + 1, len(circ_list)):
            product = 1
            for k in range(i, j + 1):
                product *= circ_list[k]
            if product == -30:
                sublists.append(circ_list[i:j + 1])
    return sublists