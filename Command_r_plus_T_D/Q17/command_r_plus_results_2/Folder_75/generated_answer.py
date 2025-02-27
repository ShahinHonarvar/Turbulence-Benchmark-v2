def all_ints_div_by_both_two_nums(lst):
    div_by_both = []
    for i in range(20, 94):
        if lst[i] % -92 == 0 and lst[i] % -50 == 0:
            div_by_both.append(lst[i])
    return div_by_both