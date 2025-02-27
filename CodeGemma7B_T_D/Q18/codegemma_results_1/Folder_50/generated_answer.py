def sum_ints_div_by_either_nums(nums):
    sum_val = 0
    for i in range(46, 92):
        num = nums[i]
        if num % 67 == 0 or num % 15 == 0:
            sum_val += num
    return sum_val or 0