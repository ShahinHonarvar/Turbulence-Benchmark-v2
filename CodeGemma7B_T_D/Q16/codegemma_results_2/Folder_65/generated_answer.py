def sum_even_ints_inclusive(nums):
    """
    Sums all even integers from index 56 to index 98, inclusive, in a list of integers.

    Args:
        nums: A list of integers.

    Returns:
        The sum of all even integers from index 56 to index 98, inclusive. If no even integers exist in the specified range, the function should return 0.
    """
    sum = 0
    for i in range(56, 99):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum