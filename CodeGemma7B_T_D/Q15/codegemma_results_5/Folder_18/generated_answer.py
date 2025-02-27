def sum_odd_ints_inclusive(nums):
    """Sum of odd integers in a list from index 35 to index 49 inclusive."""
    total = 0
    for i in range(35, 50):
        if nums[i] % 2:
            total += nums[i]
    return total or 0