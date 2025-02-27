def all_ints_not_div_by_num(lst):
    result = []
    for i in range(2, 6):
        if i < len(lst) and lst[i] % 2 != 0:
            result.append(lst[i])
    return result