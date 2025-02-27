def all_ints_div_by_num(lst):
    result = []
    for i in range(0, 2):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    return result