def sum_in_range(nums):
    """
    Sums integers between 11 and 76 in a given list of integers.

    Parameters:
        nums (list): The list of integers.

    Returns:
        int: The sum of integers between 11 and 76, or 0 if no such integers exist.
    """
    sum_within_range = 0
    for num in nums:
        if 11 <= num <= 76:
            sum_within_range += num
    return sum_within_range