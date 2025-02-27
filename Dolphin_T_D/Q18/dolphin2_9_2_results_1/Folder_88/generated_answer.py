def sum_ints_div_by_either_nums(nums):
    sum_ints = 0
    for i in range(3, 10):
        if nums[i] % 6 == 0 or nums[i] % 1 == 0:
            sum_ints += nums[i]
    return sum_ints