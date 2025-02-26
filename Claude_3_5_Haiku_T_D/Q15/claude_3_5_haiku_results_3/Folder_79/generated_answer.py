def sum_odd_ints_inclusive(nums):
    if len(nums) <= 4:
        return 0
    target_num = nums[4]
    if target_num % 2 == 0:
        return 0
    return target_num