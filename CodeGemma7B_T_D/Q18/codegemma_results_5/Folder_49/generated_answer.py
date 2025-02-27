def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for i in range(80, 201):
        if nums[i] % 10 == 0 or nums[i] % 1000 == 0:
            sum_nums += nums[i]
    if sum_nums == 0:
        return 0
    return sum_nums