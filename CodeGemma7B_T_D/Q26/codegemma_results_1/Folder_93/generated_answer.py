def sum_in_range(nums):
    """
    Calculates the sum of integers in a list that are between -23 and 64, inclusive.

    Args:
    nums: A list of integers.

    Returns:
    The sum of integers in the list that are between -23 and 64, inclusive. If the given list does not contain such integers, the function returns 0.
    """
    sum_in_range = 0
    for num in nums:
        if -23 <= num <= 64:
            sum_in_range += num
    return sum_in_range