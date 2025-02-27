def all_neg_ints_exclusive(nums):
    """
    Returns a list of negative integers from index 86 to index 90, both exclusive.

    Args:
        nums: A list of integers.

    Returns:
        A list of negative integers from index 86 to index 90, both exclusive. If no negative integers exist in the specified range, the function returns an empty list.
    """
    neg_nums = []
    for num in nums[86:90]:
        if num < 0:
            neg_nums.append(num)
    return neg_nums