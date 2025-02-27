def all_ints_div_by_num(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] % 4 == 0:
            result.append(lst[i])
    return result