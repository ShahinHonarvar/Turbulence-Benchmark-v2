def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(25, 81):
        if nums[i] % 20 == 0 or nums[i] % 26 == 0:
            sum += nums[i]
    if sum == 0:
        return 0
    return sum