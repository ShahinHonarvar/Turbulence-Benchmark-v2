def all_ints_div_by_num(lst):
    value = 14
    result = []
    for i in range(43, 77):
        if lst[i] % value == 0:
            result.append(lst[i])
    return result