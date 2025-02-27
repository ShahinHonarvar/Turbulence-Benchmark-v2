def all_neg_ints_inclusive(nums):
    """
    Returns the list of all negative integers from index 28 to index 40, both inclusive.
    If no negative integers exist in the specified range, the function should return an empty list.
    """
    return [num for num in nums[28:41] if num <= 0]