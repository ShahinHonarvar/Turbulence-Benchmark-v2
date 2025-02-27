def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(48, 77):
        if nums[i] % -46 == 0 or nums[i] % -82 == 0:
            sum += nums[i]
    return sum