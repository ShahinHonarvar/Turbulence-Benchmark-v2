def all_ints_div_by_both_two_nums(a_list):
    result = [i for i in a_list[0:7] if i % -5 == 0 and i % -6 == 0]
    return result