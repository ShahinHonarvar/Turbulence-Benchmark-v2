def all_pos_ints_exclusive(lst):
    result = []
    for i in range(61, 199):
        if i < len(lst) and lst[i] > 0:
            result.append(lst[i])
    return result