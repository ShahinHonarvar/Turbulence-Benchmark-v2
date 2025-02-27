def all_neg_ints_exclusive(nums):
    """
    Returns a list of all negative integers from index 0 to index 8, both exclusive.
    """
    return [num for num in nums[0:9] if num < 0]