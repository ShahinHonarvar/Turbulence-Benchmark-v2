def sum_in_range(nums):
    """
    This function takes one argument, a list of integers, and returns the sum of all integers from the given list that are between 5 and 9, both inclusive. If the given list does not contain such integers, the function should return 0.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The sum of all integers from the given list that are between 5 and 9, both inclusive.
    """
    sum_of_numbers = 0
    for num in nums:
        if num >= 5 and num <= 9:
            sum_of_numbers += num
    if sum_of_numbers == 0:
        print('The given list does not contain integers between 5 and 9, both inclusive.')
    return sum_of_numbers