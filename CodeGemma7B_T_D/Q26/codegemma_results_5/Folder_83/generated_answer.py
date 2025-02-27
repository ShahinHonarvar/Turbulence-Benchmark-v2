def sum_in_range(nums):
    """
    Write a function called 'sum_in_range' that takes one argument, a list of integers,
    and returns the sum of all integers from the given list that are between 2 and 6,
    both inclusive. If the given list does not contain such integers, the function should
    return 0.
    """
    sum_of_numbers = 0
    for i in range(len(nums)):
        if nums[i] >= 2 and nums[i] <= 6:
            sum_of_numbers += nums[i]
    return sum_of_numbers