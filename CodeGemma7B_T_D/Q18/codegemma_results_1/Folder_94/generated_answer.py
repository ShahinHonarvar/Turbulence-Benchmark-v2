def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(93, 95):
        if nums[i] % -53 == 0 or nums[i] % -91 == 0:
            sum += nums[i]
    return sum