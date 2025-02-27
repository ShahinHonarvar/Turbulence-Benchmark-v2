def sum_in_range(nums):
    """
    Returns the sum of all integers from a list of integers that are between 68 and 99, both inclusive.

    Args:
        nums: A list of integers.

    Returns:
        The sum of all integers from the given list that are between 68 and 99, both inclusive. If the given list does not contain such integers, the function should return 0.
    """
    total = 0
    for num in nums:
        if num >= 68 and num <= 99:
            total += num
    return total