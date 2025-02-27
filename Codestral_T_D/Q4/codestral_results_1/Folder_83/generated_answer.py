def all_pos_ints_exclusive(lst):
    if len(lst) < 200:
        return []
    else:
        return [num for num in lst[90:200] if num > 0]