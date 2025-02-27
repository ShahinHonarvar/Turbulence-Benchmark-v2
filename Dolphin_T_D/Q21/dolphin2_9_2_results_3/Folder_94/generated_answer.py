def all_ints_div_by_num(lst):
    result = []
    for i in range(18, 94):
        if lst[i] % -85 == 0:
            result.append(lst[i])
    return result