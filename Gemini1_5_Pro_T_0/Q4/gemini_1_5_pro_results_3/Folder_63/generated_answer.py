def all_pos_ints_exclusive(lst):
    result = []
    for i in range(39, 52):
        if i >= len(lst):
            break
        if lst[i] > 0:
            result.append(lst[i])
    return result