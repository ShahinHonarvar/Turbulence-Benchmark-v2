def all_ints_not_div_by_num(lst):
    result = []
    for i in range(84, 86):
        if lst[i] % 99 != 0:
            result.append(lst[i])
    return result