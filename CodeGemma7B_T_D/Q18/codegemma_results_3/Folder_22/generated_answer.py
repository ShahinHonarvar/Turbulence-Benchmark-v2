def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for i in range(40, 201):
        if i % 21 == 0 or i % 71 == 0:
            sum_nums += nums[i - 21]
    if sum_nums == 0:
        return 0
    else:
        return sum_nums