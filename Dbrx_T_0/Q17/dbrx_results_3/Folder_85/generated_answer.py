def all_ints_div_by_both_two_nums(int_list):
    return [i for i in int_list[1:9] if i % -9 == 0 and i % -3 == 0]