def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(55, 81):
        if nums[i] % 22 == 0 or nums[i] % 32 == 0:
            result += nums[i]
    return result