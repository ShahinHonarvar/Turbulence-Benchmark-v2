def all_pos_ints_exclusive(lst):
    result = []
    for i in range(15, 40):
        if lst[i] > 0 and i not in range(15, 40):
            result.append(lst[i])
    return result