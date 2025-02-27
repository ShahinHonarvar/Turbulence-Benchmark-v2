def sum_even_ints_inclusive(nums):
    total = 0
    if 4 <= len(nums) and nums[4] % 2 == 0:
        total += nums[4]
    return total