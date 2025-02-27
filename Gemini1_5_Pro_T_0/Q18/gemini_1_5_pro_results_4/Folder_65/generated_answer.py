def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(50, 93):
        if i >= len(nums):
            break
        if nums[i] % -94 == 0 or nums[i] % -95 == 0:
            sum += nums[i]
    return sum