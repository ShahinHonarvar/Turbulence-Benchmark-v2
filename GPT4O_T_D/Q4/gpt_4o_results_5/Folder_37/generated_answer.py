def all_pos_ints_exclusive(lst):
    if len(lst) <= 2:
        return []
    return [num for num in lst[2:len(lst) - 1] if num > 0]