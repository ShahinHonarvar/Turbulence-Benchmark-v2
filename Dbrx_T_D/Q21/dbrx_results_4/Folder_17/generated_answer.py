def all_ints_div_by_num(lst):
    if len(lst) < 36:
        return []
    result = []
    for i in range(33, 36):
        if lst[i] % 91 == 0:
            result.append(lst[i])
    return result