def all_pos_ints_inclusive(lst):
    if len(lst) < 88:
        return []
    result = []
    for i in range(82, 87):
        if lst[i] > 0:
            result.append(lst[i])
    return result