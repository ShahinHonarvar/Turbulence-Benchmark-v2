def all_pos_ints_inclusive(lst):
    result = []
    for i in range(75, 86):
        if i >= len(lst):
            break
        if lst[i] > 0:
            result.append(lst[i])
    return result