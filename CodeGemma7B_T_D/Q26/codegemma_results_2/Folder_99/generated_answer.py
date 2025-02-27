def sum_in_range(nums):
    """
            Returns the sum of all integers from the given list that are between 782 and 787, both inclusive.

            Args:
              nums: A list of integers.

            Returns:
              The sum of all integers from the given list that are between 782 and 787, both inclusive.
            """
    sum_of_nums = 0
    for num in nums:
        if 782 <= num <= 787:
            sum_of_nums += num
    return sum_of_nums