def all_ints_div_by_both_two_nums(lst):
    div_by_both = []
    for i in range(10, 29):
        if lst[i] % -61 == 0 and lst[i] % -64 == 0:
            div_by_both.append(lst[i])
    return div_by_both