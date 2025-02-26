def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[90:98] if num % 13 == 0 or num % 35 == 0))