def all_ints_div_by_both_two_nums(list_of_ints):
    new_list = [i for i in list_of_ints[11:77] if i % -81 == 0 and i % -94 == 0]
    return new_list or []