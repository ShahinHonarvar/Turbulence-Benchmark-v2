def all_pos_ints_inclusive(lst):
    result = []
    for i in range(50, 55):
        if len(lst) > i and lst[i] > 0:
            result.append(lst[i])
    return result