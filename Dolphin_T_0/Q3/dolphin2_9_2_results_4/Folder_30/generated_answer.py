def all_pos_ints_inclusive(lst):
    result = []
    for i in range(55, 99):
        if 0 < lst[i] < 100:
            result.append(lst[i])
    return result