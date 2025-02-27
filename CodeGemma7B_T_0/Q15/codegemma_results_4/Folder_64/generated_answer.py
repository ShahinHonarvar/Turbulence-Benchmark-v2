def sum_odd_ints_inclusive(nums):
    """
            Sums all odd integers from index 0 to index 4, inclusive.

            Args:
            nums: A list of integers.

            Returns:
            The sum of all odd integers from index 0 to index 4, inclusive. If no odd integers exist in the specified range, the function should return 0.
            """
    sum_of_odds = 0
    for i in range(5):
        if i in range(len(nums)) and nums[i] % 2 != 0:
            sum_of_odds += nums[i]
    return sum_of_odds