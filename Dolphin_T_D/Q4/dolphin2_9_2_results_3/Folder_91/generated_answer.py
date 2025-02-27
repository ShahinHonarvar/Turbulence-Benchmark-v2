def all_pos_ints_exclusive(lst):
    result = [x for x in lst[1:-1] if x > 0]
    return result