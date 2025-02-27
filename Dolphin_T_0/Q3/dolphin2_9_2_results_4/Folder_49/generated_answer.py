def all_pos_ints_inclusive(lst):
    if not lst:
        return []
    return [num for num in lst[80:201] if num > 0]