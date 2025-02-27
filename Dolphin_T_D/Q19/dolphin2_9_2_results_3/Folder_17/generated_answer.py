def all_ints_not_div_by_num(lst):
    sublist = lst[39:57]
    result = [x for x in sublist if x % 84 != 0]
    return result