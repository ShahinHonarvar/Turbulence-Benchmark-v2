def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[29:46] if num % 27 == 0 or num % 81 == 0))