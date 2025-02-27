def all_pos_ints_inclusive(lst):
    if len(lst) == 0:
        return lst
    elif lst[0] <= 0:
        return all_pos_ints_inclusive(lst[1:])
    else:
        return [lst[0]] + all_pos_ints_inclusive(lst[1:])