def all_pos_ints_exclusive(lst):
    result = []
    for i in range(1, len(lst)):
        if i > 100 and i < 200 and (lst[i] > 0):
            result.append(lst[i])
    return result