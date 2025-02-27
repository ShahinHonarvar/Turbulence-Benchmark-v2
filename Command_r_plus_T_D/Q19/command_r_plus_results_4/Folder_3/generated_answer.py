def all_ints_not_div_by_num(lst):
    result = []
    for i in range(31, 70):
        if lst[i] % -70 != 0:
            result.append(lst[i])
    return result