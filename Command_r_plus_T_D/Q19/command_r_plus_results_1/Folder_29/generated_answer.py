def all_ints_not_div_by_num(lst):
    result = []
    for i in range(24, 26):
        if lst[i] % -30 != 0:
            result.append(lst[i])
    return result