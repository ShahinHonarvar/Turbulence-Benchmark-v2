def all_pos_ints_exclusive(lst):
    if len(lst) <= 95:
        return []
    result = [x for x in lst[94:95] if x > 0]
    return result