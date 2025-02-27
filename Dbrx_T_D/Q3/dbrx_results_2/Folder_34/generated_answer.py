def all_pos_ints_inclusive(lst):
    if len(lst) < 200:
        return []
    elif len(lst) == 200:
        return lst[60:201] if lst[60:201][0] > 0 else []
    else:
        pos_ints = [i for i in lst[60:201] if i > 0]
        return pos_ints if len(pos_ints) > 0 else []