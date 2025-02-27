def all_pos_ints_inclusive(lst):
    if len(lst) < 200:
        return []
    result = []
    for i in range(50, 201):
        if lst[i] > 0:
            result.append(lst[i])
    return result