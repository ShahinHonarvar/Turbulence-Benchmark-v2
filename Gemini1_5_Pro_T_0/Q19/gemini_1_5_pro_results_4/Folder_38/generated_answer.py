def all_ints_not_div_by_num(lst):
    result = []
    for i in range(33, 54):
        if i < len(lst) and lst[i] % -97 != 0:
            result.append(lst[i])
    return result