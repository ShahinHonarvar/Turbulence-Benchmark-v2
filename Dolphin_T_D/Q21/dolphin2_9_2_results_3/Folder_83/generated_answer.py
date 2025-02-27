def all_ints_div_by_num(lst):
    result = []
    for i in range(40, 401):
        if i % 7 == 0:
            result.append(lst[i])
    return result