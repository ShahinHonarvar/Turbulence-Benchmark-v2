def lists_with_product_equal_n(circular_list):
    """
    The function takes as input a circular list of integers and returns a list of contiguous substrings
    of the circular list such that their product is equal to a given number.
    """
    required_product = -87
    sublists = []
    current_sublist = []
    current_product = 1
    for i in range(len(circular_list)):
        current_sublist.append(circular_list[i])
        current_product *= circular_list[i]
        while current_product > required_product:
            current_product /= current_sublist[0]
            current_sublist.pop(0)
        if current_product == required_product:
            sublists.append(current_sublist[:])
    return sublists