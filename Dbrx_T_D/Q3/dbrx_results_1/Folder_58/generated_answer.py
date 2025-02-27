def all_pos_ints_inclusive(lst):
    if len(lst) < 556:
        return []
    result = []
    for i in range(209, 557):
        if lst[i] > 0:
            result.append(lst[i])
    return result