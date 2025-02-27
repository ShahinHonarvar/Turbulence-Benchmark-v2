def sum_odd_ints_inclusive(nums):
    """
            Sums all odd integers from index 0 to index 10, inclusive.

            Args:
                nums: A list of integers.

            Returns:
                The sum of all odd integers from index 0 to index 10, inclusive. If no odd integers exist in the specified range, the function should return 0.
            """
    sum_of_odd_ints = 0
    for i in range(len(nums)):
        if i >= 0 and i <= 10 and (nums[i] % 2 != 0):
            sum_of_odd_ints += nums[i]
    if sum_of_odd_ints == 0:
        return 0
    return sum_of_odd_ints