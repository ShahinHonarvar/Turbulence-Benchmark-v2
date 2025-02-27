def sum_odd_ints_inclusive(nums):
    if len(nums) > 1:
        if nums[1] % 2 != 0:
            return nums[1]
    return 0