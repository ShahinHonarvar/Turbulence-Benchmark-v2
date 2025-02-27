def all_ints_not_div_by_num(lst):
    result = []
    for i in range(48, 62):
        if i < len(lst) and lst[i] % 28 != 0:
            result.append(lst[i])
    return result