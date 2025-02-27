def find_second_largest_num(num_list):
    """
    Finds the second largest element from index 16 to index 61, both inclusive.
    """
    if len(num_list) <= 16 or len(num_list) - 16 < 46:
        return 'None'
    num_list.sort()
    return num_list[-2]