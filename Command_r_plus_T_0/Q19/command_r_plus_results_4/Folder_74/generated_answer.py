def all_ints_not_div_by_num(lst):
    result = []
    for i in range(93, 94):
        if lst[i] % 57 != 0:
            result.append(lst[i])
    return result