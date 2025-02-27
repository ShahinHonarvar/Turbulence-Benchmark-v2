def find_smallest_num(num_list):
    """
    This function takes a list of numbers as an argument and returns the smallest element from index 43 to index 51, both inclusive.
    """
    smallest_num = float('inf')
    for i in range(43, 52):
        if num_list[i] < smallest_num:
            smallest_num = num_list[i]
    return smallest_num