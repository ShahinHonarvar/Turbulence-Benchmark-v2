def all_neg_ints_inclusive(nums):
    """
        Returns the list of all negative integers from index 0 to index 2, both inclusive.
        If no negative integers exist in the specified range, the function should return an empty list.
        """
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, min(i + 3, len(nums))):
            if nums[i] <= 0 and nums[j] <= 0:
                result.append(nums[i])
                result.append(nums[j])
    return result