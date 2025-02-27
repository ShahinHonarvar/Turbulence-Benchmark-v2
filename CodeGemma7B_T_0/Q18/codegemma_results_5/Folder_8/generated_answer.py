def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(36, 86):
        if nums[i] % 27 == 0 or nums[i] % 96 == 0:
            sum += nums[i]
    if sum == 0:
        return 0
    return sum