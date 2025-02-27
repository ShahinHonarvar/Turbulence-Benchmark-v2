def sum_even_ints_inclusive(nums):
    """
            Sums all even integers from index 30 to index 87, inclusive.

            Args:
            nums: A list of integers.

            Returns:
            The sum of all even integers from index 30 to index 87, inclusive. If no even integers exist in the specified range, the function should return 0.
            """
    sum = 0
    for i in range(30, 88):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum