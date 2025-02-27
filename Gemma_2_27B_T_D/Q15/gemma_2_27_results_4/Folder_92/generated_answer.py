def sum_odd_ints_inclusive(nums):
    if 1 < len(nums) and nums[1] % 2 != 0:
        return nums[1]
    return 0