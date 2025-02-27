def sum_ints_div_by_either_nums(nums):
    sum = 0
    for x in range(13, 19):
        if nums[x] % 45 == 0 or nums[x] % 20 == 0:
            sum += nums[x]
    return sum or 0