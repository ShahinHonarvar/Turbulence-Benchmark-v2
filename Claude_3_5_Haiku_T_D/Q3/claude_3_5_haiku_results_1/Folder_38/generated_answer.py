def all_pos_ints_inclusive(lst):
    if len(lst) <= 22:
        return []
    positive_ints = [num for num in lst[22:64] if num > 0]
    return positive_ints