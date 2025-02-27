def all_neg_ints_inclusive(nums):
    """Returns a list of negative integers from index 533 to index 605, inclusive.
    If no negative integers exist in the specified range, the function should return an empty list.
    """
    return [num for num in nums[533:606] if num < 0]