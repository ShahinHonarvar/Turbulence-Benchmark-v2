def sum_odd_ints_inclusive(nums):
    if len(nums) < 5:
        return 0
    if nums[4] % 2 == 0:
        return 0
    return nums[4]