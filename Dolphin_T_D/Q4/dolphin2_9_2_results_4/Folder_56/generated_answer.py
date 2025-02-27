def all_pos_ints_exclusive(lst):
    result = []
    for i in range(8, 10):
        if i < len(lst) and 1 <= lst[i] <= 100:
            result.append(lst[i])
    return result