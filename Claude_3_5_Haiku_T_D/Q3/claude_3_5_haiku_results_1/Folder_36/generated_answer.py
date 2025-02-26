def all_pos_ints_inclusive(lst):
    if len(lst) <= 750:
        return []
    return [x for x in lst[246:751] if x > 0]