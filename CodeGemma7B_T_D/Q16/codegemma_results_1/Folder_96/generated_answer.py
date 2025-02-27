def sum_even_ints_inclusive(nums):
    """
    Sums all even integers from index 50 to index 200, inclusive, in the given list.

    Args:
        nums: A list of integers.

    Returns:
        The sum of all even integers from index 50 to index 200, inclusive. If no even integers exist in the specified range, returns 0.
    """
    total = 0
    for i in range(50, 201):
        if nums[i] % 2 == 0:
            total += nums[i]
    return total