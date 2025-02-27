def all_ints_div_by_num(lst):
    result = []
    for i in range(161, 971):
        if lst[i] % 763 == 0:
            result.append(lst[i])
    return result