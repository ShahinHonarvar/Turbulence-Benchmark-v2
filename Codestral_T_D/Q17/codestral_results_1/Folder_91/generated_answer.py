def all_ints_div_by_both_two_nums(int_list):
    return [x for x in int_list[0:5] if x % 8 == 0 and x % -3 == 0]