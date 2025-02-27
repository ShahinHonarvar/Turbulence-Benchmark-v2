def sum_ints_div_by_either_nums(nums):
    total = 0
    for i in range(6):
        if i % -1 == 0 or i % 13 == 0:
            total += nums[i]
    return total