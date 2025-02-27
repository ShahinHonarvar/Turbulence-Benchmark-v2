def all_pos_ints_inclusive(lst):
    if len(lst) < 82 or 56 > len(lst):
        return []
    return [i for i in lst[56:83] if i > 0]