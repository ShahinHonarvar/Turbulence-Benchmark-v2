def all_ints_div_by_num(lst):
    result = []
    for i in range(13, 69):
        if lst[i] % 71 == 0:
            result.append(lst[i])
    return result