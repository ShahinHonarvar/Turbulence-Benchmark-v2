def all_pos_ints_inclusive(lst):
    if len(lst) <= 774:
        return []
    subset = lst[667:775]
    return [num for num in subset if num > 0]