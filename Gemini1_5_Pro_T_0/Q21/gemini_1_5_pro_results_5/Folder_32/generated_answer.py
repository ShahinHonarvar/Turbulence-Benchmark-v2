def all_ints_div_by_num(lst):
    result = []
    for i in range(38, 56):
        if i < len(lst) and lst[i] % 31 == 0:
            result.append(lst[i])
    return result