def sum_odd_ints_inclusive(nums):
    """
    Calculates the sum of all odd integers from index 62 to index 92 (inclusive) in a list.

    Args:
        nums: A list of integers.

    Returns:
        The sum of all odd integers from index 62 to index 92, inclusive. Returns 0 if no odd integers exist in the specified range.
    """
    num = nums[62:93]
    odd_nums = []
    for i in num:
        if i % 2 != 0:
            odd_nums.append(i)
    if not odd_nums:
        return 0
    else:
        return sum(odd_nums)