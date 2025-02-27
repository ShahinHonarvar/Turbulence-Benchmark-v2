def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(50, 93):
        if i < len(nums) and (nums[i] % -94 == 0 or nums[i] % -95 == 0):
            total += nums[i]
    return total