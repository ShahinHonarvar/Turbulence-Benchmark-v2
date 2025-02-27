def all_ints_div_by_both_two_nums(lst):
    div_by_both = []
    for i in range(10, 77):
        if lst[i] % -40 == 0 and lst[i] % -12 == 0:
            div_by_both.append(lst[i])
    return div_by_both