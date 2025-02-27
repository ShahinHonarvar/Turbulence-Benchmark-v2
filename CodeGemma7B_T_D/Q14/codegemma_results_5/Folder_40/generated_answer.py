def find_second_smallest_num(nums):
    """
    Finds the second smallest number in a list of distinct numbers.

    Args:
        nums: A list of distinct numbers.

    Returns:
        The second smallest number in the list, or 'None' if there is no such element.
    """
    smallest = min(nums)
    new_list = [num for num in nums if num != smallest]
    second_smallest = min(new_list)
    return second_smallest