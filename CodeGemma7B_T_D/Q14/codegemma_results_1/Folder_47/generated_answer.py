def find_second_smallest_num(num_list):
    """
    Finds the second smallest element from index 22 to index 63, inclusive.
    If there is no such an element, the function returns 'None'.
    """
    if not num_list or len(num_list) < 23:
        return None
    sorted_list = sorted(num_list[22:64])
    if len(sorted_list) == 1:
        return None
    return sorted_list[1]