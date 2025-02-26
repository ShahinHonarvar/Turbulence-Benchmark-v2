def sum_odd_ints_inclusive(nums):
    if len(nums) <= 300:
        return 0
    target_num = nums[300]
    return target_num if target_num % 2 != 0 else 0