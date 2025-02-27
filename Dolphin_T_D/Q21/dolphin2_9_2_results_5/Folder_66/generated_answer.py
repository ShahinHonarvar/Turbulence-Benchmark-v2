def all_ints_div_by_num(lst):
    result = []
    for i in range(14, 69):
        if lst[i] % 18 == 0:
            result.append(lst[i])
    return result