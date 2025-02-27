def sum_ints_div_by_either_nums(lst):
    if len(lst) < 4:
        lst = lst[:len(lst)]
    else:
        lst = lst[:4]
    return sum((x for x in lst if x % 11 == 0 or x % -7 == 0))