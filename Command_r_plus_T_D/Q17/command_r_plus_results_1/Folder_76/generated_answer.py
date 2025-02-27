def all_ints_div_by_both_two_nums(int_list):
    result = [i for i in int_list[250:630] if i % 850 == 0 and i % 587 == 0]
    return result