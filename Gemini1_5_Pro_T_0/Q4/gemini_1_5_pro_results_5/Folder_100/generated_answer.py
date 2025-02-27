def all_pos_ints_exclusive(lst):
    result = []
    for i in range(23, 24):
        if i >= 0 and i < len(lst) and (lst[i] > 0):
            result.append(lst[i])
    return result