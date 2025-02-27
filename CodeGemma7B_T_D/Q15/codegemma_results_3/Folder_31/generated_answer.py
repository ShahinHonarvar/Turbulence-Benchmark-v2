def sum_odd_ints_inclusive(nums):
    """
            Sums all odd integers from index 75 to index 88, inclusive.

            Args:
            nums: A list of integers.

            Returns:
            The sum of all odd integers from index 75 to index 88, inclusive. If no odd integers exist in the specified range, the function should return 0.
            """
    has_odds = False
    odd_sum = 0
    for i in range(75, 89):
        if nums[i] % 2 != 0:
            has_odds = True
            odd_sum += nums[i]
    if has_odds:
        return odd_sum
    else:
        return 0