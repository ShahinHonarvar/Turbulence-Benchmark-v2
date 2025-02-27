def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(0, 6):
        if nums[i] % -1 == 0 or nums[i] % 13 == 0:
            total += nums[i]
    if total == 0:
        return 0
    else:
        return total