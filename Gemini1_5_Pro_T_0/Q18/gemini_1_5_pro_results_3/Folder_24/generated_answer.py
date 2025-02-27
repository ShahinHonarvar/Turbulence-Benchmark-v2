def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(29, 54):
        if i >= len(nums):
            break
        if nums[i] % -68 == 0 or nums[i] % -85 == 0:
            sum += nums[i]
    return sum