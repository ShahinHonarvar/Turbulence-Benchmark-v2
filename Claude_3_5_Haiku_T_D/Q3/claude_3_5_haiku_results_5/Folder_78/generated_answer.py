def all_pos_ints_inclusive(lst):
    if len(lst) <= 51:
        return []
    positive_integers = [num for num in lst[43:52] if num > 0]
    return positive_integers