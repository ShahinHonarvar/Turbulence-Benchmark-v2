def all_neg_ints_inclusive(lst):
    result = [x for x in lst[246:750] if x < 0]
    if not result:
        return []
    return result