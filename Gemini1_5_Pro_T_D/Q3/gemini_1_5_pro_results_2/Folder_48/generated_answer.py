def all_pos_ints_inclusive(lst):
    result = []
    for i in range(max(533, 0), min(len(lst), 606)):
        if lst[i] > 0:
            result.append(lst[i])
    return result