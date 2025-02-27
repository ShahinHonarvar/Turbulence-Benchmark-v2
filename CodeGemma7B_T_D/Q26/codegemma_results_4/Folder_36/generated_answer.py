def sum_in_range(nums):
    """
            Sums all integers from a list that are between 465 and 927, both inclusive.

            Args:
                nums: A list of integers.

            Returns:
                The sum of all integers from the given list that are between 465 and 927, both inclusive. If the given list does not contain such integers, the function should return 0.
            """
    sum_of_nums = 0
    for num in nums:
        if num >= 465 and num <= 927:
            sum_of_nums += num
    return sum_of_nums