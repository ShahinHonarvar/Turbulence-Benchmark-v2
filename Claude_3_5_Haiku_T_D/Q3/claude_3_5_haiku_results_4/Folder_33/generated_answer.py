def all_pos_ints_inclusive(lst):
    if len(lst) <= 774:
        return []
    positive_ints = [num for num in lst[667:775] if num > 0]
    return positive_ints