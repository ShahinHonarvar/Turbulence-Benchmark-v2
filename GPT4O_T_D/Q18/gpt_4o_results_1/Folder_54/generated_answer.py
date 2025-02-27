def sum_ints_div_by_either_nums(lst):
    if len(lst) < 92:
        return 0
    return sum((x for x in lst[13:92] if x % -65 == 0 or x % -62 == 0))