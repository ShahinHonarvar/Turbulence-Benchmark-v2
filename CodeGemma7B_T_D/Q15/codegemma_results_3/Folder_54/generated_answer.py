def sum_odd_ints_inclusive(nums):
    """
    Calculates the sum of all odd integers from index 34 to index 55, inclusive, in a given list of integers.

    Args:
    nums: A list of integers.

    Returns:
    The sum of all odd integers from index 34 to index 55, inclusive, or 0 if no such integers exist.
    """
    if not nums or len(nums) < 34 or len(nums) <= 55:
        return 0
    odd_nums = [num for num in nums[34:56] if num % 2 != 0]
    if not odd_nums:
        return 0
    return sum(odd_nums)