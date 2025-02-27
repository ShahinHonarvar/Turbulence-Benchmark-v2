def all_ints_div_by_num(lst):
    result = []
    for i in range(11, 83):
        if lst[i] % -47 == 0:
            result.append(lst[i])
    return result