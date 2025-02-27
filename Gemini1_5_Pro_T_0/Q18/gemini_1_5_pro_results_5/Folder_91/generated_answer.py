def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(min(len(nums), 5)):
        if nums[i] % 8 == 0 or nums[i] % -3 == 0:
            sum += nums[i]
    return sum