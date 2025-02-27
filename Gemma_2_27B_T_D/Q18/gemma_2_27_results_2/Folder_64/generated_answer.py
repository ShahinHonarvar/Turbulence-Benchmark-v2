def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(4):
        if nums[i] % 11 == 0 or nums[i] % -7 == 0:
            sum += nums[i]
    return sum