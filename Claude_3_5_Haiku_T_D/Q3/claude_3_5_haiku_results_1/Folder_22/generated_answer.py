def all_pos_ints_inclusive(lst):
    if len(lst) <= 200:
        return []
    result = [num for num in lst[40:201] if num > 0]
    return result