def all_pos_ints_inclusive(lst):
    if len(lst) < 5:
        return []
    positive_ints = [num for num in lst[4:5] if num > 0]
    return positive_ints