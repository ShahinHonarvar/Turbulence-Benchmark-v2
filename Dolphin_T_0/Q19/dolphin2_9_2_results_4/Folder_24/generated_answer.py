def all_ints_not_div_by_num(lst):
    result = []
    for i in range(41, 69):
        if i >= 0 and i % -82 != 0:
            result.append(lst[i])
    return result