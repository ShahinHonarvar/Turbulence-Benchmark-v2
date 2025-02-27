def all_pos_ints_exclusive(lst):
    if len(lst) < 5:
        return []
    else:
        return [i for i in lst[1:5] if i > 0]