def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(38, 53):
        if nums[i] % -41 == 0 or nums[i] % -47 == 0:
            total += nums[i]
    return total