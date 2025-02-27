def all_pos_ints_exclusive(lst):
    pos_ints = []
    for i in range(27, 34):
        if i < len(lst) and i >= 0 and (lst[i] > 0):
            pos_ints.append(lst[i])
    return pos_ints