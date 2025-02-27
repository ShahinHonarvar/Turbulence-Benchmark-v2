def all_ints_div_by_num(lst):
    if len(lst) > 0 and lst[0] % 4 == 0:
        return [lst[0]]
    else:
        return []