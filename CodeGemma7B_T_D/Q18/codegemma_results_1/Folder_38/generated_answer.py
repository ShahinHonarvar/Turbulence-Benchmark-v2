def sum_ints_div_by_either_nums(nums):
    num_list = nums[10:77]
    sum_val = 0
    for num in num_list:
        if num % 40 == 0 or num % 12 == 0:
            sum_val += num
    if sum_val == 0:
        return 0
    else:
        return sum_val