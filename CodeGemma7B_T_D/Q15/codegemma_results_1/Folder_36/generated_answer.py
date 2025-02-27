def sum_odd_ints_inclusive(nums):
    """
            Sums all odd integers from index 246 to index 750, inclusive.

            Args:
                nums: A list of integers.

            Returns:
                The sum of all odd integers from index 246 to index 750, inclusive. If no odd integers exist in the specified range, the function should return 0.
            """
    if not nums or len(nums) < 246 or len(nums) < 750:
        return 0
    total = 0
    for i in range(246, 751):
        if i < len(nums) and nums[i] % 2 != 0:
            total += nums[i]
    return total