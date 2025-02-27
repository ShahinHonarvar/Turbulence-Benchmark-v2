def all_pos_ints_inclusive(lst):
    try:
        return [x for x in lst[62:64] if x > 0]
    except IndexError:
        return []