def sum_odd_ints_inclusive(nums):
    if len(nums) < 2:
        return 0
    elif nums[1] % 2 == 1:
        return nums[1]
    else:
        return 0