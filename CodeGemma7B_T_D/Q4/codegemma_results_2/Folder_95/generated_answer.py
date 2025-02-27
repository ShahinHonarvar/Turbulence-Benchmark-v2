def all_pos_ints_exclusive(lst):
    range_start = 25
    range_end = 80
    posit_int_lst = list()
    for i in lst:
        if range_start <= i < range_end and i > 0:
            posit_int_lst.append(i)
    return posit_int_lst