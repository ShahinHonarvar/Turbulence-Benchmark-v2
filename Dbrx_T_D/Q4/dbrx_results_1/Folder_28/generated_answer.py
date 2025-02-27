def all_pos_ints_exclusive(lst):
    if len(lst) < 52 or len(lst) < 20:
        return []
    return [i for i in lst[20:51] if i > 0]