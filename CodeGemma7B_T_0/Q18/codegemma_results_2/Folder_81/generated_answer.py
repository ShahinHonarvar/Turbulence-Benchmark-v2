def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(10, 101):
        if i % 10 == 0 or i % 100 == 0:
            sum += nums[i]
    return sum