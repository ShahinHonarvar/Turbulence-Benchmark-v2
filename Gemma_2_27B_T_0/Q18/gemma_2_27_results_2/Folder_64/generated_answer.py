def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(4):
        if nums[i] % 11 == 0 or nums[i] % -7 == 0:
            total += nums[i]
    return total