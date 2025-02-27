def all_ints_div_by_num(lst):
    result = []
    for i in range(3):
        if lst[i] % 3 == 0:
            result.append(lst[i])
    return result