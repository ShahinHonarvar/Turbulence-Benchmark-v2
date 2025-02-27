def all_pos_ints_inclusive(lst):
    if lst[0] > 0:
        return [i for i in lst if i > 0]
    else:
        return []