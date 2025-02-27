def all_pos_ints_inclusive(lst):
    if len(lst) < 35 or 31 > len(lst):
        return []
    else:
        return [i for i in lst[31:35] if i > 0]