def all_pos_ints_inclusive(lst):
    result = []
    for i in range(56, 99):
        if 0 < lst[i] < 100:
            result.append(lst[i])
    return result