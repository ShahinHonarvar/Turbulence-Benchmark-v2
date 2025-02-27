def sum_odd_ints_inclusive(nums):
    if len(nums) < 7:
        return 0
    elif nums[6] % 2 == 0:
        return 0
    else:
        return nums[6]