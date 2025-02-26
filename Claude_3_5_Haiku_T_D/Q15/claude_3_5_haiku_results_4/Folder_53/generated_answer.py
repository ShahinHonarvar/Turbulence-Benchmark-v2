def sum_odd_ints_inclusive(nums):
    if len(nums) <= 300:
        return 0
    if nums[300] % 2 == 1:
        return nums[300]
    return 0