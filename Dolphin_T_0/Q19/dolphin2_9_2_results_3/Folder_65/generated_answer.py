def all_ints_not_div_by_num(lst):
    result = []
    for i in range(15, 51):
        if i % -34 != 0:
            result.append(lst[i])
    return result