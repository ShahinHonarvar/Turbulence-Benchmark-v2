def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(8, 10):
        if nums[i] in [-3, 6]:
            sum += nums[i]
    return sum or 0