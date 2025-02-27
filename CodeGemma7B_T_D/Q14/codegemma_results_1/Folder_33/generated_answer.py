def find_second_smallest_num(num_list):
    """
    Returns the second smallest element from index 262 to index 746, both inclusive. If there is no such an element, the function should return 'None'.
    """
    sorted_list = sorted(num_list[262:747])
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None