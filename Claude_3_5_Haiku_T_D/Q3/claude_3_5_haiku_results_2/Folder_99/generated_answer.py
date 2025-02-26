def all_pos_ints_inclusive(lst):
    if len(lst) <= 370:
        return []
    result = [num for num in lst[310:371] if num > 0]
    return result