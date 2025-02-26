def all_pos_ints_inclusive(lst):
    if len(lst) <= 975:
        return []
    result = [x for x in lst[639:976] if x > 0]
    return result