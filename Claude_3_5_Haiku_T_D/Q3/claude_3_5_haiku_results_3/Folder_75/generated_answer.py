def all_pos_ints_inclusive(lst):
    if len(lst) <= 57:
        return []
    pos_ints = [num for num in lst[56:58] if num > 0]
    return pos_ints