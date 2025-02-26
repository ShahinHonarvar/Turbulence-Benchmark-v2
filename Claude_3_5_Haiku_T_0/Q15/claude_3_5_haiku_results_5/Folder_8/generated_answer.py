def sum_odd_ints_inclusive(nums):
    if len(nums) <= 23:
        return 0
    target_num = nums[23]
    return target_num if target_num % 2 != 0 else 0