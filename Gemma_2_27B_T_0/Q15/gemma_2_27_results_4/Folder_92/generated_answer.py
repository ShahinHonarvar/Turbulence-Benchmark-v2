def sum_odd_ints_inclusive(nums):
    if 1 >= len(nums) or nums[1] % 2 == 0:
        return 0
    return nums[1]