def all_ints_not_div_by_num(lst):
    result = []
    for i in range(17, 88):
        if i % -75 != 0:
            result.append(lst[i])
    return result