def all_ints_div_by_both_two_nums(lst):
    div_by_neg9_and_neg7 = []
    for i in lst[7:10]:
        if i % -9 == 0 and i % -7 == 0:
            div_by_neg9_and_neg7.append(i)
    return div_by_neg9_and_neg7