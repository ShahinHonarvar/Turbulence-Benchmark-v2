def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(40, 201):
        if i % 21 == 0 or i % 71 == 0:
            sum += nums[i]
    return sum