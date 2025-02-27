def all_pos_ints_exclusive(lst):
    result = []
    for i in range(56 + 1, 88):
        if lst[i] > 0:
            result.append(lst[i])
    return result