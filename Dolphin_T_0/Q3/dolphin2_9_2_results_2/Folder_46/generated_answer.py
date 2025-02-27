def all_pos_ints_inclusive(lst):
    result = []
    for i in range(30, 88):
        if lst[i] > 0:
            result.append(lst[i])
    return result