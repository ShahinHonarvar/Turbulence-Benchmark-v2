def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(38, 53):
        if i >= len(nums):
            break
        if nums[i] % -41 == 0 or nums[i] % -47 == 0:
            sum += nums[i]
    return sum