def sum_odd_ints_inclusive(nums):
    if len(nums) > 1 and nums[1] % 2 != 0:
        return nums[1]
    else:
        return 0