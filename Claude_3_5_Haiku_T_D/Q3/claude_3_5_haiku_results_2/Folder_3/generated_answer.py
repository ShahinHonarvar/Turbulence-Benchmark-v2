def all_pos_ints_inclusive(lst):
    if len(lst) <= 92:
        return []
    positive_ints = [num for num in lst[62:93] if num > 0]
    return positive_ints