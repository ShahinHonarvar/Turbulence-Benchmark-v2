def all_ints_div_by_num(lst):
    result = []
    for i in range(0, 2 + 1):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    if len(result) == 0:
        return []
    else:
        return result