def all_pos_ints_inclusive(lst):
    if not isinstance(lst, list) or len(lst) < 95:
        return []
    return [i for i in lst[74:96] if i > 0]