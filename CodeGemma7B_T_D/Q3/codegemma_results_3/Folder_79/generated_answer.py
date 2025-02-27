def all_pos_ints_inclusive(lst):
    result = []
    for i in range(4, len(lst) + 1):
        if i >= 4 and i <= len(lst) and (lst[i - 1] > 0):
            result.append(lst[i - 1])
    if len(result) == 0:
        return []
    else:
        return result