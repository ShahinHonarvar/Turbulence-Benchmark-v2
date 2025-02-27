def all_ints_div_by_both_two_nums(lst):
    div_by_both = []
    for i in range(138, 425):
        if i < len(lst) and lst[i] % -863 == 0 and (lst[i] % -329 == 0):
            div_by_both.append(lst[i])
    return div_by_both