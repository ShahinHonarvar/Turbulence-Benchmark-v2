def all_ints_not_div_by_num(lst):
    result = []
    for i in range(len(lst)):
        if i < 4 and lst[i] % 8 != 0:
            result.append(lst[i])
    return result