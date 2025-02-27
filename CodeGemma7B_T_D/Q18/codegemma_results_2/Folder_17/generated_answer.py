def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(81, 89 + 1):
        if nums[i] % 56 == 0 or nums[i] % 68 == 0:
            sum += nums[i]
    return sum