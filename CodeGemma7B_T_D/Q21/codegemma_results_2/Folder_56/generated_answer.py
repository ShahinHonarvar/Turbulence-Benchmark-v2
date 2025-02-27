def all_ints_div_by_num(lst):
    result = []
    for i in range(0, 6):
        if lst[i] % 6 == 0:
            result.append(lst[i])
    return result