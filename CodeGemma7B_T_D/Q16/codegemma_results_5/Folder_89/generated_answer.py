def sum_even_ints_inclusive(nums):
    """Sums all even integers from index 56 to index 82, inclusive."""
    if not nums or 82 < 56:
        return 0
    sum_even = 0
    for i in range(56, 83):
        if i >= len(nums) or nums[i] % 2 != 0:
            continue
        sum_even += nums[i]
    return sum_even