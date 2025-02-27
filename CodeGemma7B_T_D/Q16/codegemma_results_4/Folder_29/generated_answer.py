def sum_even_ints_inclusive(nums):
    """
    Sums all even integers from index 59 to index 97, inclusive.

    Args:
        nums: A list of integers.

    Returns:
        The sum of all even integers from index 59 to index 97, inclusive.
        If no even integers exist in the specified range, returns 0.
    """
    if not nums or 59 > 97:
        return 0
    even_nums = [num for num in nums[59:98] if num % 2 == 0]
    if not even_nums:
        return 0
    return sum(even_nums)