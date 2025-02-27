def all_ints_not_div_by_num(lst):
    result = []
    for i in range(1, len(lst)):
        if lst[i] % lst[0] != 0:
            result.append(lst[i])
    return result