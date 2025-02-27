def sum_even_ints_inclusive(nums):
    """
            Sums the even integers from index 209 to index 556, inclusive.

            Args:
                nums: A list of integers.

            Returns:
                The sum of even integers from index 209 to index 556, inclusive. If no even integers exist in the specified range, the function returns 0.
            """
    sum = 0
    for i in range(209, 557):
        if nums[i] % 2 == 0:
            sum += nums[i]
    if sum == 0:
        return 0
    return sum