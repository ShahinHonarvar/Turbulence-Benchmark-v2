def all_ints_not_div_by_num(lst):
    result = []
    for i in range(38, 81):
        if i in lst and i % 49 != 0:
            result.append(i)
    return result