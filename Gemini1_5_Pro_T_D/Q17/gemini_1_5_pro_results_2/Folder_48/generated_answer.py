def all_ints_div_by_both_two_nums(lst):
    new_lst = []
    for i in range(306, 958):
        if i >= len(lst):
            break
        if lst[i] % 982 == 0 and lst[i] % 319 == 0:
            new_lst.append(lst[i])
    return new_lst