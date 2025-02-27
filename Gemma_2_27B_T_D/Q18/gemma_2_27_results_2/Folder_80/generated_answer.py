def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(14, 94):
        if nums[i] % 71 == 0 or nums[i] % 81 == 0:
            total += nums[i]
    return total