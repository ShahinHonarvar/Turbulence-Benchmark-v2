def sum_odd_ints_inclusive(nums):
    """
            Sums all odd integers from index 0 to index 10, inclusive.

            Args:
                nums: A list of integers.

            Returns:
                The sum of all odd integers from index 0 to index 10, inclusive. If no odd integers exist in the specified range, the function should return 0.
            """
    sum_odd = 0
    for i in range(11):
        if i % 2 != 0 and i >= 0 and (i <= 10):
            sum_odd += nums[i]
    return sum_odd