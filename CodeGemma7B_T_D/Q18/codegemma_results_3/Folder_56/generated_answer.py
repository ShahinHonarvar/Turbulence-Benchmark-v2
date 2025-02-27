def sum_ints_div_by_either_nums(nums):
    result = 0
    for i in range(7, 10):
        if nums[i] % 9 == 0 or nums[i] % 7 == 0:
            result += nums[i]
    if result == 0:
        return 0
    return result