def all_pos_ints_inclusive(lst):
    result = []
    for i in range(max(0, min(len(lst) - 1, 10)), min(len(lst), 101)):
        if lst[i] > 0:
            result.append(lst[i])
    return result