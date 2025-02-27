def sum_in_range(nums):
    """
            This function takes one argument, a list of integers, and returns the sum of all integers from the given list that are between 2 and 3, both inclusive. If the given list does not contain such integers, the function should return 0.
            """
    sum_nums = 0
    for num in nums:
        if 2 <= num <= 3:
            sum_nums += num
    return sum_nums