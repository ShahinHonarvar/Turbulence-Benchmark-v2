def all_ints_div_by_both_two_nums(lst):
    temp_lst = lst[12:18]
    div_lst = [i for i in temp_lst if i % 45 == 0 and i % 20 == 0]
    return div_lst