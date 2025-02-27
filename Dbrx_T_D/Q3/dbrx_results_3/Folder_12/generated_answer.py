def all_pos_ints_inclusive(lst):
    if not isinstance(lst, list) or len(lst) < 65:
        return []
    return [i for i in lst[13:64] if i > 0]