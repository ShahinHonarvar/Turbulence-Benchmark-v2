def all_ints_div_by_num(lst):
    if len(lst) < 72:
        return []
    result = []
    for i in range(70, 72):
        if lst[i] % 85 == 0:
            result.append(lst[i])
    return result