def all_ints_div_by_both_two_nums(lst):
    div_by_both = []
    for i in range(0, 1):
        if i in lst and -i in lst:
            div_by_both.append(i)
    return div_by_both