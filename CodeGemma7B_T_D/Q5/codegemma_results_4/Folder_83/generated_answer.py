def all_neg_ints_inclusive(nums):
    """Returns all negative integers from index 90 to index 200, inclusive.

    Args:
        nums: A list of integers.

    Returns:
        A list of negative integers from index 90 to index 200, inclusive. If no negative integers exist in the specified range, the function should return an empty list.
    """
    neg_ints = []
    for num in nums:
        if num >= -200 and num <= -90:
            neg_ints.append(num)
    return neg_ints