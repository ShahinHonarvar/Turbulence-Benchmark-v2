def all_pos_ints_exclusive(lst):
    if len(lst) >= 2 and lst[1] > 0 and (lst[2] > 0):
        return list(range(1, lst[2]))
    elif len(lst) >= 2 and lst[1] > 0 and (lst[2] <= 0):
        return list(range(1, 0))
    else:
        return []