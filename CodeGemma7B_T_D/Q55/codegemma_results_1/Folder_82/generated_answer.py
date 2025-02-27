def lists_with_product_equal_n(circular_list):
    """
    This function returns a list of sublists each of which contains the contiguous integers from the given list such that their product equals 4.
    
    Args:
        circular_list: a circular list of integers
    
    Returns:
        a list of sublists each of which contains the contiguous integers from the given list such that their product equals 4. If no such sublist exists, the function should return an empty list. If there are duplicates of such a sublist, they should all be contained in the returned list. The order of sublists in the returned list does not matter.
    """
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            product = circular_list[i]
            for k in range(j + 1, len(circular_list) + i):
                index = k % len(circular_list)
                product *= circular_list[index]
                if product == 8:
                    sublists.append(circular_list[i:index + 1])
                elif product > 8:
                    break
    return sublists