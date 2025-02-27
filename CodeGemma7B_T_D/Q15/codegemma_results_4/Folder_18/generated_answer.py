def sum_odd_ints_inclusive(nums):
    """Sums odd integers from index 35 to 49, inclusive."""
    total = 0
    for i in range(35, 50):
        if i % 2 != 0:
            total += nums[i]
    return total if total else 0