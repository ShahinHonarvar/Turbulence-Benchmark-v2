def sum_odd_ints_inclusive(nums):
    total = 0
    if 6 <= len(nums) and nums[6] % 2 != 0:
        total += nums[6]
    return total