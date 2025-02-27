def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(46, 92):
        if nums[i] % 67 == 0 or nums[i] % 15 == 0:
            result += nums[i]
    return result