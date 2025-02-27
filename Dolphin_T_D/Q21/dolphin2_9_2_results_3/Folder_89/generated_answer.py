def all_ints_div_by_num(lst):
    result = []
    for i in range(30, 60):
        if lst[i] % 39 == 0:
            result.append(lst[i])
    return result