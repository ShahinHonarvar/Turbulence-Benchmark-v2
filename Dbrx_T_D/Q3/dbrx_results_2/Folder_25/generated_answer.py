def all_pos_ints_inclusive(lst):
    if len(lst) < 93:
        return []
    result = []
    for i in range(29, 94):
        if lst[i] > 0:
            result.append(lst[i])
    return result