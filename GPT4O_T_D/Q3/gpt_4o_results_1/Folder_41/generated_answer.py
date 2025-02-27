def all_pos_ints_inclusive(lst):
    if len(lst) > 6:
        positive_ints = [x for x in lst[6:7] if x > 0]
    else:
        positive_ints = []
    return positive_ints