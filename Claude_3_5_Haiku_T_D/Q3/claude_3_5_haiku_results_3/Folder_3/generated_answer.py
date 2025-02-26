def all_pos_ints_inclusive(lst):
    if len(lst) < 93:
        return []
    filtered_list = [num for num in lst[62:93] if num > 0]
    return filtered_list