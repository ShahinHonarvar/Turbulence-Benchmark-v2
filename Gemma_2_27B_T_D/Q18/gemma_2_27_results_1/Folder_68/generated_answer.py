def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(7, 8):
        if nums[i] % 5 == 0 or nums[i] % 7 == 0:
            sum += nums[i]
    return sum