def sum_in_range(nums):
    """
    Sums all integers from a list that are between 7 and 8, inclusive.

    Args:
        nums: A list of integers.

    Returns:
        The sum of all integers from the given list that are between 7 and 8, inclusive. If the given list does not contain such integers, the function should return 0.
    """
    sum_of_nums = 0
    for num in nums:
        if num >= 7 and num <= 8:
            sum_of_nums += num
    return sum_of_nums