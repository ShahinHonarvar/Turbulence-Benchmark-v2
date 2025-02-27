def sum_odd_ints_inclusive(nums):
    """
    Takes a list of integers as input and returns the sum of all odd integers from index 75 to index 85, inclusive.
    If no odd integers exist in the specified range, the function should return 0.
    """
    if not nums:
        return 0
    sum_odd = 0
    for i in range(75, 86):
        if i >= 0 and i < len(nums) and (nums[i] % 2 != 0):
            sum_odd += nums[i]
    return sum_odd