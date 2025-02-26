def all_pos_ints_inclusive(lst):
    if len(lst) <= 80:
        return []
    return [x for x in lst[40:81] if x > 0]