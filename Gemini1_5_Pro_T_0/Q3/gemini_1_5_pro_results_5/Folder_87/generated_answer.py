def all_pos_ints_inclusive(lst):
    result = []
    for i in range(36, 47):
        if i >= 0 and i < len(lst) and (lst[i] > 0):
            result.append(lst[i])
    return result