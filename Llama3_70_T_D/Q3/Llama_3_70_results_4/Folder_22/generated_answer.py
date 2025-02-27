def all_pos_ints_inclusive(lst):
    return [lst[i] for i in range(40, 201) if i < len(lst) and lst[i] > 0]