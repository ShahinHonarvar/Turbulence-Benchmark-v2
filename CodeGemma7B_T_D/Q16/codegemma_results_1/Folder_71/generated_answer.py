def sum_even_ints_inclusive(nums):
    """
    Sums all even integers from index 26 to index 52, inclusive. If no even integers exist in the specified range, the function returns 0.
    Args:
        nums: A list of integers.
    Returns:
        The sum of all even integers from index 26 to index 52, inclusive.
    """
    s = 0
    for i in range(26, 53):
        if nums[i] % 2 == 0:
            s += nums[i]
    return s