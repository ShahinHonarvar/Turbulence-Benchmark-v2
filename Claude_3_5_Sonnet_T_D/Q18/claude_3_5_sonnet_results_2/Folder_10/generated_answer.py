def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[32:100] if num % -11 == 0 or num % -15 == 0))