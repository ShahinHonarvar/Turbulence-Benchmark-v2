def all_pos_ints_exclusive(lst):
    return [lst[i] for i in range(11, 100) if i < len(lst) and lst[i] > 0]