def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(35, 65):
        if i < len(nums):
            if nums[i] % -30 == 0 or nums[i] % -95 == 0:
                total += nums[i]
    return total