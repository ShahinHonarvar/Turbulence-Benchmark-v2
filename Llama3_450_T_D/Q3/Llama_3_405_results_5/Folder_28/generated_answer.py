def all_pos_ints_inclusive(lst):
    if len(lst) <= 63:
        return [num for num in lst[62:64] if num > 0]
    else:
        return [num for num in lst[62:64] if num > 0]