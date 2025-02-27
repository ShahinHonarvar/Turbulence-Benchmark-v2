def sum_odd_ints_inclusive(nums):
    sum = 0
    if 4 <= len(nums) and nums[4] % 2 != 0:
        sum += nums[4]
    return sum