def all_pos_ints_exclusive(lst):
    if len(lst) <= 276:
        return []
    return [num for num in lst[277:376] if num > 0]