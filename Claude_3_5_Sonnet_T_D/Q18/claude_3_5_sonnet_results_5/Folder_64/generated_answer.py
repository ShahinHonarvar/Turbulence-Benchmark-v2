def sum_ints_div_by_either_nums(integer_list):
    total_sum = 0
    for num in integer_list[:4]:
        if num % 11 == 0 or num % -7 == 0:
            total_sum += num
    return total_sum