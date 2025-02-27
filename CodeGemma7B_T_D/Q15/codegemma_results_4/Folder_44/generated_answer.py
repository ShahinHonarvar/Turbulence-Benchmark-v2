def sum_odd_ints_inclusive(nums):
    """
    Sums all odd integers from index 13 to index 68, inclusive.

    Args:
    nums: A list of integers.

    Returns:
    The sum of all odd integers from index 13 to index 68, inclusive. If no odd
    integers exist in the specified range, the function should return 0.
    """
    count = 0
    for i in range(13, 69):
        if i % 2 != 0:
            count += nums[i]
    if count == 0:
        return 0
    else:
        return count