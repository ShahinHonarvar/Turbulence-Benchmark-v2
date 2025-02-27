def all_pos_ints_exclusive(lst):
    result = []
    for i in range(20, 44):
        if i not in lst:
            result.append(i)
    return result