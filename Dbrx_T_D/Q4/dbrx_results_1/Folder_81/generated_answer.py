def all_pos_ints_exclusive(lst):
    if len(lst) < 100:
        return []
    result = []
    for i in range(10, 100):
        if lst[i] > 0:
            result.append(lst[i])
    return result