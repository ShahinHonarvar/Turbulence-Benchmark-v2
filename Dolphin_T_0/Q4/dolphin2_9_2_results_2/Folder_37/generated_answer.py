def all_pos_ints_exclusive(lst):
    result = []
    for i in lst[1:3]:
        if i > 0:
            result.append(i)
    return result