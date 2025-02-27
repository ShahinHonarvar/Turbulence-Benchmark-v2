def all_pos_ints_inclusive(lst):
    if len(lst) < 2:
        return []
    return [i for i in range(lst[0], lst[1] + 1) if i > 0]