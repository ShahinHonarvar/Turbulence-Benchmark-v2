def lists_with_product_equal_n(circular_list):
    """This function takes an argument, a circular list of integers.
    In a circular list, the head and the tail are adjacent to each other to form a circle.
    The function should return a list of sublists each of which contains the contiguous integers from the given list such that their product equals -8. 
    Each sublist in the returned list can be of any size as long as it is smaller than or equal to the size of the given list.
    If no such sublist exists, the function should return an empty list.
    If there are duplicates of such a sublist, they should all be contained in the returned list. 
    The order of sublists in the returned list does not matter."""
    sublists = []
    current_sublist = []
    current_product = 1
    for i in range(len(circular_list)):
        current_sublist.append(circular_list[i])
        current_product *= circular_list[i]
        while current_product == -8:
            sublists.append(current_sublist[:])
            current_product //= circular_list[i - len(current_sublist) + 1]
            current_sublist.pop(0)
        if i == len(circular_list) - 1:
            current_product //= circular_list[0]
            current_sublist.pop(0)
    return sublists