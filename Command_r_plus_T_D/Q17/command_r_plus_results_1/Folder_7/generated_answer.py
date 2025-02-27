def all_ints_div_by_both_two_nums(lst):
    div_by_both = []
    for i in range(543, 585):
        if lst[i] % -553 == 0 and lst[i] % -737 == 0:
            div_by_both.append(lst[i])
    return div_by_both