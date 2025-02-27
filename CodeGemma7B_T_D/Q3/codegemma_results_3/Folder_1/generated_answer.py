def all_pos_ints_inclusive(lst):
    result = []
    for i in range(31, 73):
        if i >= len(lst) or lst[i] <= 0:
            continue
        result.append(lst[i])
    return result