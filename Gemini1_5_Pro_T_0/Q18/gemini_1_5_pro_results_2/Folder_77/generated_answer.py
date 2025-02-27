def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(828, 933):
        if i >= len(nums):
            break
        if nums[i] % -649 == 0 or nums[i] % -461 == 0:
            sum += nums[i]
    return sum