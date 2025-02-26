def all_pos_ints_inclusive(lst):
    if len(lst) <= 6:
        return []
    positive_ints = [num for num in lst[6:7] if num > 0]
    return positive_ints