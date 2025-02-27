def sum_even_ints_inclusive(nums):
    """Calculates the sum of even integers from index 19 to 92 in a list."""
    total_sum = 0
    for i in range(19, 93):
        if nums[i] % 2 == 0:
            total_sum += nums[i]
    return total_sum