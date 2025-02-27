def all_ints_div_by_num(lst):
    result = []
    for i in range(20, 201):
        if i < len(lst) and lst[i] % 4 == 0:
            result.append(lst[i])
    return result