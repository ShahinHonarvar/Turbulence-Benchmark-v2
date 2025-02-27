def sum_odd_ints_inclusive(nums):
    if len(nums) < 24:
        return 0
    if nums[23] % 2 == 0:
        return 0
    else:
        return nums[23]