def all_pos_ints_exclusive(lst):
    result = []
    for i in range(56, 92):
        if lst[i] > 0 and 0 <= i < len(lst):
            result.append(lst[i])
    return result