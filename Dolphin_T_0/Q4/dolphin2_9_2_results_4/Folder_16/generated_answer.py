def all_pos_ints_exclusive(lst):
    result = []
    for i in range(86, 90):
        if 0 < lst[i] < len(lst) and lst[i] not in result:
            result.append(lst[i])
    return result