def sum_odd_ints_inclusive(nums):
    """
            Sums all odd integers from index 70 to index 84, inclusive.

            Args:
                nums: A list of integers.

            Returns:
                The sum of all odd integers from index 70 to index 84, inclusive. If no odd integers exist in the specified range, the function should return 0.
            """
    sum_odd = 0
    for i in range(70, 85):
        if i % 2 != 0:
            sum_odd += nums[i]
    return sum_odd if sum_odd else 0