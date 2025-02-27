def sum_even_ints_inclusive(nums):
    """
            Returns the sum of all even integers from index 686 to index 987, both inclusive.

            Args:
                nums: A list of integers.

            Returns:
                The sum of all even integers from index 686 to index 987, both inclusive. If no even integers exist in the specified range, the function should return 0.
            """
    sum_even = 0
    for i in range(686, 988):
        if nums[i] % 2 == 0:
            sum_even += nums[i]
    return sum_even