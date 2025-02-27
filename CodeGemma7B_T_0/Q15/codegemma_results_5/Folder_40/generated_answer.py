def sum_odd_ints_inclusive(nums):
    """
            Sums all odd integers from index 0 to index 2, both inclusive.

            Args:
                nums: A list of integers.

            Returns:
                The sum of all odd integers from index 0 to index 2, both inclusive. If no odd integers exist in the specified range, the function should return 0.
            """
    sum_of_odd_ints = 0
    for i in range(len(nums)):
        if i in [0, 1, 2] and nums[i] % 2 != 0:
            sum_of_odd_ints += nums[i]
    return sum_of_odd_ints