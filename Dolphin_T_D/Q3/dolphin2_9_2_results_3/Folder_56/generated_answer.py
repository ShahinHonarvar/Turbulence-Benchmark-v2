def all_pos_ints_inclusive(lst):
    if lst[0] > 0:
        return [i for i in lst[0:1] if i > 0]
    else:
        return []