def all_pos_ints_inclusive(lst):
    inclusive_list = [x for x in lst[29:80] if x > 0]
    return inclusive_list if any(inclusive_list) else []