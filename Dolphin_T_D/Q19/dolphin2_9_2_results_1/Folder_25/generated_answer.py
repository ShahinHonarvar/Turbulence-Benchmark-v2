def all_ints_not_div_by_num(lst):
    result = []
    for i in range(29, 53):
        if i not in lst:
            continue
        if lst[i] % -68 != 0:
            result.append(lst[i])
    return result