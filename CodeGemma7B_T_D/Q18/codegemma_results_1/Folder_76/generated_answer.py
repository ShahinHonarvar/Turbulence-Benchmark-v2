def sum_ints_div_by_either_nums(nums):
    output = 0
    for i in range(250, 630):
        if nums[i] % 850 == 0 or nums[i] % 587 == 0:
            output += nums[i]
    return output