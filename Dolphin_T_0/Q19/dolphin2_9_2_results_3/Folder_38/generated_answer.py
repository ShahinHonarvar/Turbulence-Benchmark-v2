def all_ints_not_div_by_num(lst):
    result = []
    for i in range(32, 54):
        if i % -97 != 0:
            result.append(lst[i])
    return result