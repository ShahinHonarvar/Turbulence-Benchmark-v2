def all_pos_ints_exclusive(lst):
    if len(lst) < 98:
        return []
    return [n for n in lst[70:98] if n > 0]