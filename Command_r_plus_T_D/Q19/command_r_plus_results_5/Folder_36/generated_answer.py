def all_ints_not_div_by_num(lst):
    result = []
    for i in range(472, 827):
        if lst[i] % 602 != 0:
            result.append(lst[i])
    return result