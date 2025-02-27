def all_ints_not_div_by_num(lst):
    result = []
    for i in range(32, 54):
        if i in lst and i % -97 != 0:
            result.append(i)
    return result