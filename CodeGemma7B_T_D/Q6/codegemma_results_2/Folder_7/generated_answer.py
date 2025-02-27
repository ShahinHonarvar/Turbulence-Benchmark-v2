def all_neg_ints_exclusive(nums):
    """
    Returns the list of all negative integers from index 323 to index 972, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    result = []
    for i in range(len(nums)):
        if nums[i] < 0 and 323 < i < 972:
            result.append(nums[i])
    return result