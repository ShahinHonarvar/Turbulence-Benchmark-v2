def all_ints_div_by_both_two_nums(lst):
    new_list = []
    for i in range(0, 2):
        if lst[i] % 2 == 0 and lst[i] % 1 == 0:
            new_list.append(lst[i])
    return new_list