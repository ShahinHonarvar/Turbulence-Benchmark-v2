def all_ints_not_div_by_num(lst):
    result = []
    for i in range(35, 98):
        if len(lst) > i and lst[i] % 41 != 0:
            result.append(lst[i])
    return result