def sum_even_ints_inclusive(nums):
    """Sums even integers from index 1 to 5, inclusive."""
    total = 0
    for i in range(1, 6):
        if i in range(1, 6) and nums[i] % 2 == 0:
            total += nums[i]
    return total