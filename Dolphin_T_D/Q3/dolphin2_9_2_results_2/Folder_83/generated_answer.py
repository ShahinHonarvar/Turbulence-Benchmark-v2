def all_pos_ints_inclusive(lst):
    result = []
    for i in range(90, 201):
        if lst[i] > 0:
            result.append(lst[i])
    return result