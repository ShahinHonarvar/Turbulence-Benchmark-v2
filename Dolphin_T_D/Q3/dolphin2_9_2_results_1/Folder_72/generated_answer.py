def all_pos_ints_inclusive(lst):
    result = []
    for i in range(29, 52):
        if 0 < lst[i] < 1000:
            result.append(lst[i])
    return result