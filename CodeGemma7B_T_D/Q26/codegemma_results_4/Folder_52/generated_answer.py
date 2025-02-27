def sum_in_range(nums):
    """
    Returns the sum of all integers from a list of integers that are between -885 and -817, both inclusive. If the given list does not contain such integers, the function should return 0.
    """
    summation = 0
    for num in nums:
        if -885 <= num <= -817:
            summation += num
    return summation