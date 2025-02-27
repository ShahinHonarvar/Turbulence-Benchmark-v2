def all_ints_div_by_num(lst):
    result = []
    for i in range(87, 90):
        if lst[i] % 55 == 0:
            result.append(lst[i])
    return result