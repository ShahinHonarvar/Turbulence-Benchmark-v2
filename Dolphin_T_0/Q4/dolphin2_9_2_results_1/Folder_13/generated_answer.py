def all_pos_ints_exclusive(lst):
    result = []
    for i in range(74, 84):
        if lst[i] > 0:
            result.append(lst[i])
    return result