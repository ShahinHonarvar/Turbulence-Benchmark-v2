def sum_ints_div_by_either_nums(nums):
    summ = 0
    for i in range(25, 71):
        if nums[i] % 74 == 0 or nums[i] % 15 == 0:
            summ += nums[i]
    return summ or 0