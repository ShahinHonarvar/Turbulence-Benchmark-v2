def all_pos_ints_exclusive(lst):
    result = []
    for i in range(2, 7):
        if lst[i] > 0:
            result.append(lst[i])
    if not result:
        return []
    return result