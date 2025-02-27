def all_ints_div_by_num(lst):
    result = []
    for i in range(12, 16):
        if i < len(lst) and lst[i] % -80 == 0:
            result.append(lst[i])
    return result