def all_neg_ints_inclusive(nums):
    """
        Returns a list of all negative integers from index 29 to index 93, inclusive.
        If no negative integers exist in the specified range, the function returns an empty list.
        """
    if not any((num < 0 for num in nums)):
        return []
    return [num for num in nums[29:94] if num < 0]