def find_second_smallest_num(num_list):
    """
    Finds the second smallest element from index 66 to index 77, both inclusive.
    If there is no such an element, returns 'None'.
    """
    num_list.sort(key=int)
    if len(num_list[66:78]) < 2:
        return None
    return num_list[67]