def all_pos_ints_inclusive(lst):
    if len(lst) < 201 or len(lst) < 20:
        return []
    return [i for i in lst[20:201] if i > 0]