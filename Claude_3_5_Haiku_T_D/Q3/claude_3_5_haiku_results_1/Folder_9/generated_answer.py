def all_pos_ints_inclusive(lst):
    if len(lst) <= 200:
        return []
    positive_ints = [num for num in lst[70:201] if num > 0]
    return positive_ints