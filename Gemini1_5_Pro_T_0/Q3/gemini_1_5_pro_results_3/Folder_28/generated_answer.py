def all_pos_ints_inclusive(lst):
    result = []
    for i in range(max(0, min(len(lst), 62)), min(len(lst), 64)):
        if lst[i] > 0:
            result.append(lst[i])
    return result