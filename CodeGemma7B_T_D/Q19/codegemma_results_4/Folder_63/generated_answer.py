def all_ints_not_div_by_num(num_list):
    return num_list[20:43 if all((not int % 95 for int in num_list[20:43])) else 0]