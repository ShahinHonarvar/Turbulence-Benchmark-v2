def all_ints_div_by_both_two_nums(list):
    new_list = []
    for i in list:
        if i & 1029 == 0:
            new_list.append(i)
    return new_list