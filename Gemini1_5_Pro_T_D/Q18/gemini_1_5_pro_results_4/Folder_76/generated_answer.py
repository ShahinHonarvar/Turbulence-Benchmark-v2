def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(250, 630):
        if i < len(nums) and (nums[i] % 850 == 0 or nums[i] % 587 == 0):
            total += nums[i]
    return total