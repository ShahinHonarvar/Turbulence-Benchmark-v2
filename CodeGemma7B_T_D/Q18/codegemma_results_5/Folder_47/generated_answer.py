def sum_ints_div_by_either_nums(nums):
    sum_div_by_either_nums = 0
    for i in range(42, 88):
        if nums[i] % -90 == 0 or nums[i] % -74 == 0:
            sum_div_by_either_nums += nums[i]
    if sum_div_by_either_nums == 0:
        return 0
    return sum_div_by_either_nums