def sum_ints_div_by_either_nums(nums):
    sum_nums = 0
    for i in range(10, 80):
        if nums[i] % 74 == 0 or nums[i] % 58 == 0:
            sum_nums += nums[i]
    return sum_nums