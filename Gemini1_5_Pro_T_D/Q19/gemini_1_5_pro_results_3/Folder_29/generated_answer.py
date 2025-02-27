def all_ints_not_div_by_num(lst):
    result = []
    for i in range(24, 25):
        if i >= len(lst) or i < 0:
            continue
        if lst[i] % -30 != 0:
            result.append(lst[i])
    return result