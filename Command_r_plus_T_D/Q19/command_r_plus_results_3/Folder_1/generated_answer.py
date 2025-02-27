def all_ints_not_div_by_num(lst):
    result = []
    for i in range(21, 69):
        if lst[i] % -69 != 0:
            result.append(lst[i])
    return result