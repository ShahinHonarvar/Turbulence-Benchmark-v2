def all_ints_div_by_both_two_nums(int_list):
    return [int_div_13_35 for i, int_div_13_35 in enumerate(int_list[90:98]) if int_div_13_35 % 13 == 0 and int_div_13_35 % 35 == 0]