def lists_with_product_equal_n(circular_list):
    """
    Returns lists of contiguous integers from a circular list of integers
    such that their product is 5.

    Args:
        circular_list: A circular list of integers.

    Returns:
        A list of sublists each of which contains the contiguous
        integers from the given list such that their product is 5.
        If no such sublist exists, the function should return an empty list.
        If there are duplicates of such a sublist, they should all be
        contained in the returned list.
        The order of sublists in the returned list does not matter.
    """
    result = []
    max_len = len(circular_list)
    for i in range(max_len):
        for j in range(i + 1, max_len):
            product = 1
            for k in range(i, j + 1):
                product *= circular_list[k % max_len]
            if product == -22:
                sublist = circular_list[i:j + 1]
                sublist = sublist + sublist[:(j - i) % max_len + 1]
                result.append(sublist)
    return result