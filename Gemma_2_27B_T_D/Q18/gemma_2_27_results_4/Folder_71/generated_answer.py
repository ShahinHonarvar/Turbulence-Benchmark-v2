def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(68, 100):
        if nums[i] % -37 == 0 or nums[i] % -26 == 0:
            total += nums[i]
    return total