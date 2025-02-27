def all_pos_ints_exclusive(lst):
    result = []
    for i in range(43, 99):
        if i < len(lst) and lst[i] > 0:
            result.append(lst[i])
    return result