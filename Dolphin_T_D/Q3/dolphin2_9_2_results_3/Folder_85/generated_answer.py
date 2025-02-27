def all_pos_ints_inclusive(lst):
    result = [i for i in lst[6:9] if i > 0]
    if not result:
        return []
    else:
        return result