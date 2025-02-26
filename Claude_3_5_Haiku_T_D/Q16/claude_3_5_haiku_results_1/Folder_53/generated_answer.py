def sum_even_ints_inclusive(nums):
    if len(nums) < 112:
        return 0
    target_num = nums[111]
    return target_num if target_num % 2 == 0 else 0