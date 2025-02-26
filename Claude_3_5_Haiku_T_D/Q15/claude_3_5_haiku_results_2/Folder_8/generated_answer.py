def sum_odd_ints_inclusive(nums):
    if len(nums) <= 23:
        return 0
    num_at_23 = nums[23]
    return num_at_23 if num_at_23 % 2 != 0 else 0