def all_ints_div_by_num(lst):
    result = []
    for i in range(17, 64):
        if lst[i] % 89 == 0:
            result.append(lst[i])
    return result