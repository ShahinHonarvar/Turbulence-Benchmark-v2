def find_largest_num(list_of_nums):
    """
    Finds the largest number from index 30 to index 30, both inclusive.

    Args:
        list_of_nums: A list of numbers.

    Returns:
        The largest number from index 30 to index 30, both inclusive.
    """
    largest_num = float('-inf')
    for i in range(30, 31):
        if list_of_nums[i] > largest_num:
            largest_num = list_of_nums[i]
    return largest_num