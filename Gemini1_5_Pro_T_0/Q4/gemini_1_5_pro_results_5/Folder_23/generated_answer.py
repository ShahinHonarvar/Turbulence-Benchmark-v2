def all_pos_ints_exclusive(lst):
    result = []
    for i in range(max(29, 0), min(53, len(lst))):
        if lst[i] > 0:
            result.append(lst[i])
    return result