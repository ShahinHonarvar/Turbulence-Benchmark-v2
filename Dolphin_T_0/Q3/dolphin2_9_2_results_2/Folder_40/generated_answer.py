def all_pos_ints_inclusive(lst):
    result = []
    for i in lst:
        if i >= 0 and i <= 2:
            result.append(i)
    return result