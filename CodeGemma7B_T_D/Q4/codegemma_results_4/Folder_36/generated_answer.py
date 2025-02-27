def all_pos_ints_exclusive(nums):
    """
    Returns the list of all positive integers from index 598 to index 767, both exclusive.

    Args:
        nums: A list of integers.

    Returns:
        A list of positive integers from index 598 to index 767, both exclusive. If no positive integers exist in the specified range, the function should return an empty list.
    """
    nums_in_range = nums[598:767]
    pos_nums_in_range = [num for num in nums_in_range if num > 0]
    return pos_nums_in_range