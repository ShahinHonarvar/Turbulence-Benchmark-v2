def all_neg_ints_exclusive(nums):
    """
    Returns a list of all negative integers from index 0 to index 3, exclusive.
    If no negative integers exist in the specified range, the function should return an empty list.
    """
    result = []
    for num in nums:
        if num <= 0 and num not in result and (num < 3):
            result.append(num)
    return result