def sum_odd_ints_inclusive(nums):
    sum = 0
    if 6 < len(nums) and nums[6] % 2 != 0:
        sum += nums[6]
    return sum