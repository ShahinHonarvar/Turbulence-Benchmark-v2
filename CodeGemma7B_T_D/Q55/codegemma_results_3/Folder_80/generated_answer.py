def lists_with_product_equal_n(circular_list):
    """
    Returns a list of sublists of contiguous integers from the given circular list such that their product equals 43.
    """
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            circular_list.append(circular_list.pop(0))
            product = 1
            for k in range(j - i):
                product *= circular_list[k]
            if product == 43:
                yield circular_list[i:j + 1]