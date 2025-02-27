def all_ints_div_by_num(lst):
    result = []
    for i in range(315, 353):
        if i < len(lst) and lst[i] % -858 == 0:
            result.append(lst[i])
    return result