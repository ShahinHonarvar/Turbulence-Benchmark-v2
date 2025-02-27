def all_ints_not_div_by_num(lst):
    result = []
    for i in range(20, 35):
        if i < 0 or i >= len(lst):
            continue
        if lst[i] % -36 != 0:
            result.append(lst[i])
    return result