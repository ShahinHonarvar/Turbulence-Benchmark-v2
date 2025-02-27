def all_ints_div_by_num(lst):
    result = []
    for i in range(43, 60):
        if i in lst and i % 22 == 0:
            result.append(i)
    return result