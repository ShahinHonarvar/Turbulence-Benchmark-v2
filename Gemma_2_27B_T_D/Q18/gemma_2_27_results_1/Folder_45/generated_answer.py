def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(30, 201):
        if nums[i] % -115 == 0 or nums[i] % 115 == 0:
            total += nums[i]
    return total