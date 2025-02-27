def all_pos_ints_exclusive(lst):
    result = []
    for i in range(13, 71):
        if i in lst:
            result.append(i)
    return result if result else []