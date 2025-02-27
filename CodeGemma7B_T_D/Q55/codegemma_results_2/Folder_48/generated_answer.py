def lists_with_product_equal_n(circular_list):
    """
    This function takes an argument, a circular list of integers.
    In a circular list, the head and the tail are adjacent to each other to form a circle.
    The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals 990.
    Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list.
    If no such sublist exists, the function should return an empty list.
    If there are duplicates of such a sublist, they should all be contained in the returned list.
    The order of sublists in the returned list does not matter.
    """
    size = len(circular_list)
    for i in range(size):
        current_sublist = [circular_list[i]]
        current_product = circular_list[i]
        for j in range((i + 1) % size, i + size):
            current_product *= circular_list[j]
            current_sublist.append(circular_list[j])
            if current_product == 990:
                return current_sublist
            if len(current_sublist) > size:
                current_sublist = [circular_list[i]]
                current_product = circular_list[i]
    return []