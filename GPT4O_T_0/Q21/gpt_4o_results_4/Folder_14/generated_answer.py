def all_ints_div_by_num(lst):
    if len(lst) > 8 and lst[8] % 8 == 0:
        return [lst[8]]
    return []