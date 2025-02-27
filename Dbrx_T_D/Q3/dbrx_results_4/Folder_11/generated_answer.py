def all_pos_ints_inclusive(lst):
    if len(lst) < 52 or not lst[36:]:
        return []
    return [i for i in lst[36:52] if i > 0]