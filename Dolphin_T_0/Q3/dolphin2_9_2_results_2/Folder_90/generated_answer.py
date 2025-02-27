def all_pos_ints_inclusive(lst):
    result = [i for i in lst[262:747] if i > 0]
    if not result:
        return []
    return result