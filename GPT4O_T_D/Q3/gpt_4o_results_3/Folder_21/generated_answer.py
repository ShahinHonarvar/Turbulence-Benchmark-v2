def all_pos_ints_inclusive(lst):
    if 639 < len(lst) and 975 < len(lst):
        return [num for num in lst[639:976] if num > 0]
    return []