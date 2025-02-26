def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[24:33] if num % 35 == 0 or num % 87 == 0))