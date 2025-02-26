def sum_odd_ints_inclusive(nums):
    if len(nums) < 24:
        return 0
    target_num = nums[23]
    if target_num % 2 == 0:
        return 0
    return target_num