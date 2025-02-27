def sum_even_ints_inclusive(nums):
    total = 0
    if 29 <= len(nums) and nums[29] % 2 == 0:
        total += nums[29]
    return total