def all_ints_div_by_num(l):
    if len(l) < 8:
        return []
    result = []
    for i in range(1, 9):
        if l[i] % 6 == 0:
            result.append(l[i])
    return result