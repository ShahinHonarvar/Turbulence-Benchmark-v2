def find_smallest_num(num_list):
    """
    The function finds smallest element within a list from index 0 to 1, both inclusive.

    Parameters:
        num_list: A list of numbers.

    Returns:
        The smallest number from index 0 to 1, both inclusive.
    """
    min_num = float('inf')
    for num in num_list[0:2]:
        if num < min_num:
            min_num = num
    return min_num