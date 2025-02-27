def sum_even_ints_inclusive(nums):
    """Sums all even integers from index 62 to index 92, inclusive."""
    total_sum = 0
    for i in range(62, 93):
        if nums[i] % 2 == 0:
            total_sum += nums[i]
    return total_sum if total_sum else 0