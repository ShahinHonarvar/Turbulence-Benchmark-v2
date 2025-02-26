def all_pos_ints_inclusive(lst):
    if len(lst) < 201:
        return []
    result = [num for num in lst[100:201] if num > 0]
    return result