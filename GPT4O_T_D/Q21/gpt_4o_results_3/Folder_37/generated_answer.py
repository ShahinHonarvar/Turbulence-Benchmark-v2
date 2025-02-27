def all_ints_div_by_num(lst):
    if len(lst) > 4 and lst[4] % 3 == 0:
        return [lst[4]]
    return []