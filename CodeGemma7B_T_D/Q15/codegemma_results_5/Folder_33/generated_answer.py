def sum_odd_ints_inclusive(nums):
    """Sums all odd integers from index 667 to index 774, inclusive."""
    sum = 0
    for i in range(667, 775):
        if i % 2 != 0:
            sum += nums[i]
    return sum or 0