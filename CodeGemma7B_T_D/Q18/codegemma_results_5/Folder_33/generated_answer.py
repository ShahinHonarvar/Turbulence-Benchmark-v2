def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(281, 695):
        if nums[i] % -722 == 0 or nums[i] % -731 == 0:
            result += nums[i]
    return result or 0