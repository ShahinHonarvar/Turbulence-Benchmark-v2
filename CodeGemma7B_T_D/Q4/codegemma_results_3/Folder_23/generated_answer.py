def all_pos_ints_exclusive(nums):
    """
    This function takes one argument, a list of integers, and returns the list of all positive integers from index 29 to index 53, both exclusive.
    If no positive integers exist in the specified range, the function should return an empty list.
    """
    return [num for num in nums[29:53] if num > 0]