def sum_ints_div_by_either_nums(lst):
    if len(lst) < 77:
        return 0
    return sum((x for x in lst[13:77] if x % -66 == 0 or x % -32 == 0))