def all_pos_ints_inclusive(lst):
    return [lst[i] for i in range(9) if isinstance(lst[i], int) and lst[i] > 0]