def sum_even_ints_inclusive(nums):
    """Sums all even integers from index 29 to index 79, inclusive."""
    total = 0
    for i in range(29, 79 + 1):
        if nums[i] % 2 == 0:
            total += nums[i]
    return total