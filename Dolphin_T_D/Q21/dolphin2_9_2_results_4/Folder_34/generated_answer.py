def all_ints_div_by_num(lst):
    result = []
    for i in range(30, 31):
        if i % 3 == 0:
            result.append(lst[i])
    return result