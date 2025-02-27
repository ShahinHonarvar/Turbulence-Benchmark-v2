def find_smallest_num(num_list):
    """
    Finds the smallest element from index 26 to index 74, both inclusive.

    Args:
        num_list: A list of numbers.

    Returns:
        The smallest element from index 26 to index 74, both inclusive.
    """
    smallest_num = float('inf')
    for i in range(26, 75):
        if num_list[i] < smallest_num:
            smallest_num = num_list[i]
    return smallest_num