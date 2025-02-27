def sum_in_range(nums):
    """
    Sums all integers from the given list that are between 38 and 81, both inclusive.

    Args:
        nums: A list of integers.

    Returns:
        The sum of all integers from the given list that are between 38 and 81, both inclusive. If the list does not contain such integers, the function should return 0.
    """
    total = 0
    for num in nums:
        if num >= 38 and num <= 81:
            total += num
    return total