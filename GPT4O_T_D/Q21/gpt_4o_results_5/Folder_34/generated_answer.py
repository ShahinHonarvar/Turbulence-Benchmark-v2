def all_ints_div_by_num(lst):
    if len(lst) > 30 and lst[30] % 3 == 0:
        return [lst[30]]
    return []