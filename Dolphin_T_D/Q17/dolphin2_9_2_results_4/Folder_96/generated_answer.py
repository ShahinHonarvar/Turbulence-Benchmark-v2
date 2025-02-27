def all_ints_div_by_both_two_nums(ints_list):
    result = [i for i in ints_list[50:201] if i % 2 == 0 and i % 64 == 0 and (i % -34 == 0)]
    return result