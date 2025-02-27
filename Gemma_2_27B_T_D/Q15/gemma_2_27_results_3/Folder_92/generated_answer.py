def sum_odd_ints_inclusive(nums):
    if len(nums) < 2:
        return 0
    if nums[1] % 2 != 0:
        return nums[1]
    return 0