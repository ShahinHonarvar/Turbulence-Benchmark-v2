def all_pos_ints_inclusive(lst):
    return [lst[i] for i in range(len(lst)) if 0 <= i <= 0 and lst[i] > 0]