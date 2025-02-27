def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(48, 60):
        if nums[i] % 88 == 0 or nums[i] % 58 == 0:
            sum += nums[i]
    return sum