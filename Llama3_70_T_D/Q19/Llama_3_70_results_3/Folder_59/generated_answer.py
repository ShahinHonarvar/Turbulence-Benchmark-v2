def all_ints_not_div_by_num(lst):
    if len(lst) < 10:
        return []
    else:
        return [i for i in lst[8:10] if i % 8 != 0]