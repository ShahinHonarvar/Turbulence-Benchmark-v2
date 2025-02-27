def all_ints_div_by_num(lst):
    result = []
    for i in range(12, 16):
        if i in lst and i % -80 == 0:
            result.append(i)
    return result