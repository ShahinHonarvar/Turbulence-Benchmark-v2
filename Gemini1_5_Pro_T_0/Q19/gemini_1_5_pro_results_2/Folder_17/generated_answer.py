def all_ints_not_div_by_num(lst):
    result = []
    for i in range(39, 57):
        if i < len(lst) and lst[i] % 84 != 0:
            result.append(lst[i])
    return result