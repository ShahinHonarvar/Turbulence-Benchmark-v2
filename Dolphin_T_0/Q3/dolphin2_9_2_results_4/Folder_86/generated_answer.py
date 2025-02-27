def all_pos_ints_inclusive(lst):
    if lst:
        return [x for x in lst[31:35] if x > 0]
    else:
        return []