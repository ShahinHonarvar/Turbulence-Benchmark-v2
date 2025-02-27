def all_ints_div_by_both_two_nums(int_list):
    return [int_div_by_both for int_div_by_both in int_list[55:89] if int_div_by_both % -59 == 0 and int_div_by_both % -79 == 0] or []