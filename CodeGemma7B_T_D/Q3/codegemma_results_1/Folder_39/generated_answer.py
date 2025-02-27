def all_pos_ints_inclusive(lst):
    if not lst or lst[20] < 0 or lst[30] <= 0:
        return []
    result = []
    for i in range(20, 31):
        if lst[i] > 0:
            result.append(lst[i])
    return result