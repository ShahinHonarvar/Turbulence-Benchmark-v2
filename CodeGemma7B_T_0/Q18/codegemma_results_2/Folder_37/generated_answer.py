def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(2, 8):
        if nums[i] % -1 == 0 or nums[i] % -7 == 0:
            sum += nums[i]
    return sum