def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(36, 86):
        if nums[i] % -27 == 0 or nums[i] % -96 == 0:
            total += nums[i]
    return total