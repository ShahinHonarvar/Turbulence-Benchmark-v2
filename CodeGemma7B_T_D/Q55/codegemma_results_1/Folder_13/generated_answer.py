def lists_with_product_equal_n(circular_list):
    """
    This function takes an argument, a circular list of integers.
    In a circular list, the head and the tail are adjacent to each other to form a circle.
    The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals 54.
    Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list.
    If no such sublist exists, the function should return an empty list.
    If there are duplicates of such a sublist, they should all be contained in the returned list.
    The order of sublists in the returned list does not matter.
    """
    sublists = {}
    for i in range(len(circular_list)):
        current_element = circular_list[i]
        current_index = i
        for j in range(i + 1, len(circular_list)):
            product = current_element * circular_list[j]
            if product == 54:
                sublist = circular_list[current_index:j + 1]
                if sublist in sublists:
                    sublists[sublist].append(current_index)
                else:
                    sublists[sublist] = [current_index]
            current_element = circular_list[j]
            current_index = j
    return list(sublists.keys())