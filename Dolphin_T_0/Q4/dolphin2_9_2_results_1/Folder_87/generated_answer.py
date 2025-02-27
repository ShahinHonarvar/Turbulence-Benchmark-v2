def all_pos_ints_exclusive(lst):
    result = [x for x in lst[32:99] if x > 0]
    return result if result else []