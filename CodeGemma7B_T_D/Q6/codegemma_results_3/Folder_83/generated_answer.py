def all_neg_ints_exclusive(nums):
    """
    Returns the list of all negative integers from index 90 to index 200, both exclusive.
    If no negative integers exist in the specified range, the function should return an empty list.
    """
    return [num for num in nums[90:200] if num < 0]