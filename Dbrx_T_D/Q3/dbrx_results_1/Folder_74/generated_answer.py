def all_pos_ints_inclusive(lst):
    if len(lst) <= 78:
        return []
    return [i for i in lst[17:79] if i > 0]