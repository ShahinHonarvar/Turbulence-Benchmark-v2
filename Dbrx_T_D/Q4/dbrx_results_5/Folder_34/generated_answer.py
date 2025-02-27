def all_pos_ints_exclusive(lst):
    if len(lst) < 200:
        return []
    result = []
    for i in range(60, 200):
        num = lst[i]
        if num > 0:
            result.append(num)
    return result