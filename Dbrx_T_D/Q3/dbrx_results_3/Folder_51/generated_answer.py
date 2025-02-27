def all_pos_ints_inclusive(lst):
    if len(lst) < 9 or len(lst) > 40:
        return []
    return [i for i in lst[1:9] if i > 0]