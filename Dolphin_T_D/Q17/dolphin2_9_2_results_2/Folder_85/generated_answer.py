def all_ints_div_by_both_two_nums(lst_ints):
    result = [i for i in lst_ints[1:9] if i % -9 == 0 and i % -3 == 0]
    return result if result else []