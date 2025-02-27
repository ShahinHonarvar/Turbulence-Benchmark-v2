def all_ints_div_by_num(lst):
    result = []
    for i in range(27, 87):
        if lst[i] % 29 == 0:
            result.append(lst[i])
    return result