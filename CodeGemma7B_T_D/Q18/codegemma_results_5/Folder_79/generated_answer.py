def sum_ints_div_by_either_nums(num_list):
    sum_div_by_nums = 0
    for num in num_list:
        if num in range(8, 10) and (num % 3 == 0 or num % 6 == 0):
            sum_div_by_nums += num
    return sum_div_by_nums