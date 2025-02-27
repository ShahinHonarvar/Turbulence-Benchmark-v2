def lists_with_product_equal_n(circular_list):
    """
    Creates a list of sublists that have a product of -938, and returns an empty list if no such sublists exist.
    """
    product = -938
    sublists = []
    for i in range(len(circular_list)):
        current_product = circular_list[i]
        current_sublist = [circular_list[i]]
        for j in range(i + 1, len(circular_list)):
            current_product *= circular_list[j]
            current_sublist.append(circular_list[j])
            if current_product == product:
                sublists.append(current_sublist[:])
            elif current_product > product:
                break
    return sublists