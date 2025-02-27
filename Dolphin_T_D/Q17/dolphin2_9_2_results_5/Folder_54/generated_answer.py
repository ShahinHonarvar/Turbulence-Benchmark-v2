def all_ints_div_by_both_two_nums(lst):
    ints_div_by_both = []
    for i in range(13, 92):
        if i % -65 == 0 and i % -62 == 0:
            ints_div_by_both.append(i)
    return ints_div_by_both