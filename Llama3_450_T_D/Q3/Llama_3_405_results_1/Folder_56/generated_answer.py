def all_pos_ints_inclusive(lst):
    if len(lst) == 0:
        return []
    start = 0
    end = 0
    pos_ints = [i for i in range(lst[start], lst[end] + 1) if i > 0]
    return pos_ints