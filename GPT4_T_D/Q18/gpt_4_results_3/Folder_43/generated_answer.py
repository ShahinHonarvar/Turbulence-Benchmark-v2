def sum_ints_div_by_either_nums(int_list):
    return sum((value for i, value in enumerate(int_list[57:86]) if value % -77 == 0 or value % -32 == 0))