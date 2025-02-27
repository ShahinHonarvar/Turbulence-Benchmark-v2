def sum_odd_ints_inclusive(nums):
    """
            Sums all odd integers from index 0 to index 10, inclusive.

            Args:
                nums: A list of integers.

            Returns:
                The sum of all odd integers from index 0 to index 10, inclusive.
            """
    sum_odd = 0
    for i in range(len(nums)):
        if i >= 0 and i <= 10 and (nums[i] % 2 != 0):
            sum_odd += nums[i]
    if sum_odd == 0:
        return 0
    return sum_odd