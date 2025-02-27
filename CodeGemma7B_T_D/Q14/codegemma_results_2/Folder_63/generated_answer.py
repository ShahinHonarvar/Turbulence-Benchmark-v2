def find_second_smallest_num(num_list):
    """
            Returns the second smallest element from index 56 to index 82, both inclusive.
            If there is no such an element, the function returns 'None'.
            """
    if not num_list or len(num_list) < 57:
        return None
    sorted_list = sorted(num_list[56:83])
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]