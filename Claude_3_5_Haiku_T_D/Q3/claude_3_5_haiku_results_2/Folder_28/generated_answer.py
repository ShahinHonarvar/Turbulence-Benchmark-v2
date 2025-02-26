def all_pos_ints_inclusive(lst):
    if len(lst) < 64:
        return []
    result = []
    for i in [62, 63]:
        if lst[i] > 0:
            result.append(lst[i])
    return result