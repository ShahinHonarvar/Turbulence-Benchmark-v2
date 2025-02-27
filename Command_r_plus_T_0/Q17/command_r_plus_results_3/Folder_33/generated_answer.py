def all_ints_div_by_both_two_nums(lst):
    div_by_both = []
    for i in range(281, 695):
        if lst[i] % -722 == 0 and lst[i] % -731 == 0:
            div_by_both.append(lst[i])
    return div_by_both