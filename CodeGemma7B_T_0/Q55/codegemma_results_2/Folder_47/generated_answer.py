def lists_with_product_equal_n(circular_list):
    """
    This function takes a circular list of integers and returns a list of sublists each of which contains the contiguous integers from the given list such that their product equals -94.
    """
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            product = circular_list[i]
            sublist = [circular_list[i]]
            for k in range(j + 1, len(circular_list)):
                product *= circular_list[k]
                sublist.append(circular_list[k])
                if product == -94:
                    sublists.append(sublist[:])
    return sublists