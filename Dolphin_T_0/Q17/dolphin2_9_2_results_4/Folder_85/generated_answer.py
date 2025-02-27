def all_ints_div_by_both_two_nums(lst):
    div_by_both = []
    for i in lst[1:9]:
        if i % -9 == 0 and i % -3 == 0:
            div_by_both.append(i)
    return div_by_both