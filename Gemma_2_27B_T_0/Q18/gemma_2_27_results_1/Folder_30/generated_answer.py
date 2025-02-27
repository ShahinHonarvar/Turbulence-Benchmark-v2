def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(11, 77):
        if nums[i] % -81 == 0 or nums[i] % -94 == 0:
            total += nums[i]
    return total