def sum_ints_div_by_either_nums(nums):
    """Return list of ints starting at index 0 and ending at index 6, inclusive, divisible by either -5 or -6"""
    sum = 0
    for i in range(0, 7):
        if nums[i] % 5 == 0 or nums[i] % 6 == 0:
            sum += nums[i]
    return sum