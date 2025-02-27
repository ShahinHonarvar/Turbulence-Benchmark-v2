def all_ints_div_by_both_two_nums(integer_list):
    return [i for i in integer_list[0:4] if i % 11 == 0 and i % -7 == 0]