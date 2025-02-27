def sum_even_ints_inclusive(nums):
    """
    Sums all even integers from index 1 to index 8, inclusive, in a list of integers.

    Args:
        nums: A list of integers.

    Returns:
        The sum of all even integers from index 1 to index 8, inclusive. If no even integers exist in the specified range, the function should return 0.
    """
    return sum([n for n in nums[1:9] if n % 2 == 0]) or 0