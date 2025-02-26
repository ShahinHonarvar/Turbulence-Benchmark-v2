def all_pos_ints_inclusive(lst):
    if len(lst) <= 987:
        return []
    result = [num for num in lst[686:988] if num > 0]
    return result