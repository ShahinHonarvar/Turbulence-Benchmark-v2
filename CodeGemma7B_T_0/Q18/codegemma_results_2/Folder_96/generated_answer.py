def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(50, 201):
        if nums[i] % 34 == 0 or nums[i] % 64 == 0:
            sum += nums[i]
    return sum