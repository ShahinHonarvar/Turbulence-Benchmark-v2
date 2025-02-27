def all_ints_not_div_by_num(lst):
    result = []
    for i in range(1, 3):
        if lst[i] % 5 != 0:
            result.append(lst[i])
    return result