def lists_with_product_equal_n(circular_list):
    """
    Write a function called 'lists_with_product_equal_n' that takes an argument, a circular list of integers.
    In a circular list, the head and the tail are adjacent to each other to form a circle.
    The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals 3.
    Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list.
    If no such sublist exists, the function should return an empty list.
    If there are duplicates of such a sublist, they should all be contained in the returned list.
    The order of sublists in the returned list does not matter.
    """
    for i in range(len(circular_list)):
        product = circular_list[i]
        current_index = i
        sublist = [circular_list[i]]
        if i + 1 < len(circular_list) and circular_list[i] == circular_list[i + 1]:
            current_index += 1
        while current_index + 1 < len(circular_list):
            current_index += 1
            product *= circular_list[current_index]
            sublist.append(circular_list[current_index])
            if product == 3:
                return sublist
    return []