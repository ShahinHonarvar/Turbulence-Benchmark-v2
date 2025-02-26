def sum_ints_div_by_either_nums(int_list):
    total_sum = 0
    for num in int_list[:5]:
        if num % 8 == 0 or num % -3 == 0:
            total_sum += num
    return total_sum