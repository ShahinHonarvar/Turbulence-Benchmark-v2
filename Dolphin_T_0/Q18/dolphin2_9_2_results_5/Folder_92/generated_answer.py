def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(0, 1):
        if nums[i] % 1 == 0 or nums[i] % -1 == 0:
            sum += nums[i]
    return sum