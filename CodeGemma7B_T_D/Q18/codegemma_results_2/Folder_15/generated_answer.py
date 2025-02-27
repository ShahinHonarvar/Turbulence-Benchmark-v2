def sum_ints_div_by_either_nums(int_nums):
    sum = 0
    for i in range(0, 3):
        if int_nums[i] % 2 == 0 or int_nums[i] % 3 == 0:
            sum += int_nums[i]
    return sum or 0