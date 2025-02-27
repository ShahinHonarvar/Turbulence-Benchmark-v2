def all_ints_div_by_num(lst):
    result = []
    for i in range(22, 64):
        if lst[i] % -61 == 0:
            result.append(lst[i])
    return result