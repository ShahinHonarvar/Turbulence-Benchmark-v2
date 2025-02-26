def sum_ints_div_by_either_nums(integer_list):
    total_sum = 0
    for num in integer_list[13:77]:
        if num % -66 == 0 or num % -32 == 0:
            total_sum += num
    return total_sum