def all_ints_not_div_by_num(lst):
    result = []
    for i in range(16, 87):
        if lst[i] % -15 != 0:
            result.append(lst[i])
    return result