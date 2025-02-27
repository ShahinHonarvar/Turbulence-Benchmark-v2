def all_pos_ints_inclusive(lst):
    results = []
    for i in range(3, 6):
        if lst[i] > 0:
            results.append(lst[i])
    return results