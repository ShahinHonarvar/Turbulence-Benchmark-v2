def sum_ints_div_by_either_nums(int_list):
    ints_div_by_13 = [num for num in int_list[90:98] if num % 13 == 0]
    ints_div_by_35 = [num for num in int_list[90:98] if num % 35 == 0]
    return sum(ints_div_by_13 + ints_div_by_35)