def all_pos_ints_inclusive(lst):
    j = 0
    result = []
    for i in range(29, 94):
        if lst[i] > 0:
            result.append(lst[i])
            j += 1
    if j == 0:
        return []
    else:
        return result