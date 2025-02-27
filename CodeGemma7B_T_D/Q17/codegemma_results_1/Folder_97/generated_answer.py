def all_ints_div_by_both_two_nums(lst):
    new_lst = []
    for i in range(58, 76):
        if lst[i] % 72 == 0 and lst[i] % 62 == 0:
            new_lst.append(lst[i])
    return new_lst