def all_neg_ints_exclusive(nums):
    """
    Returns the list of all negative integers from index 20 to index 35, both exclusive.
    If no negative integers exist in the specified range, the function should return an empty list.
    """
    return [num for num in nums[20:35] if num < 0]