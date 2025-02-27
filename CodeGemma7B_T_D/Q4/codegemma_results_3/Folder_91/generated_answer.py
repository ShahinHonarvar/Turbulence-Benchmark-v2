def all_pos_ints_exclusive(lst):
    return [item for item in lst if item > 0 and item <= 5 and (lst.index(item) < 6)]