def all_pos_ints_inclusive(lst):
    return [lst[i] for i in range(len(lst)) if lst[i] > 0 and i == 0]