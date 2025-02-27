def all_pos_ints_exclusive(lst):
    if len(lst) <= 32:
        return []
    subrange = lst[33:99]
    return [x for x in subrange if x > 0]