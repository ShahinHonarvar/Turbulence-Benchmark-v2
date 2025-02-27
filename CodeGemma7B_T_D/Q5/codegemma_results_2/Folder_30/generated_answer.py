def all_neg_ints_inclusive(nums):
    """
    Returns a list of all negative integers from index 55 to index 98, inclusive.

    Args:
    nums: A list of integers.

    Returns:
    A list of negative integers from index 55 to index 98, inclusive. If no negative integers exist in the specified range, an empty list is returned.
    """
    return [num for num in nums[55:99] if num < 0] or []