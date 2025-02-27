def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(50, 201):
        if nums[i] % -34 == 0 or nums[i] % 64 == 0:
            total += nums[i]
    return total