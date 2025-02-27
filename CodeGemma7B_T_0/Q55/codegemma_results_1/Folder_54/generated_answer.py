def lists_with_product_equal_n(circular_list):
    """
    This function takes a circular list of integers and returns a list of sublists each of which contains the contiguous integers from the given list such that their product equals -17.
    """
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if len(sublist) > 0 and sublist[0] * sublist[-1] == -17:
                sublists.append(sublist)
    return sublists