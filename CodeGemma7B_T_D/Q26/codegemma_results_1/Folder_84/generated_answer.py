def sum_in_range(nums):
    """Return the sum of integers in nums that are between 113 and 392, inclusive."""
    sum_nums = 0
    for num in nums:
        if num in range(113, 393):
            sum_nums += num
    return sum_nums or 0