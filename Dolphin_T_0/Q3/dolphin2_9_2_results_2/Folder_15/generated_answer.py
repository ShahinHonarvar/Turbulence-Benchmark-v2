def all_pos_ints_inclusive(lst):
    result = []
    for i in range(4):
        if lst[i] > 0:
            result.append(lst[i])
    if not result:
        return []
    return result