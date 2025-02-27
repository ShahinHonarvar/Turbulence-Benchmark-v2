def sum_in_range(nums):
    """Computes the sum of integers in a list that are between 4 and 6, inclusive.

            Args:
                nums: A list of integers.

            Returns:
                The sum of all integers in the list that are between 4 and 6, inclusive. If
                the list does not contain such integers, the function should return 0.
            """
    sum_ = 0
    for num in nums:
        if num >= 4 and num <= 6:
            sum_ += num
    return sum_