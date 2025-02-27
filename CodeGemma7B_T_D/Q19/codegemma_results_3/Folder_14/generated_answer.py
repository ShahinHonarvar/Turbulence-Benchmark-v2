def all_ints_not_div_by_num(list):
    result = []
    for i in range(2, 7):
        if list[i] % 8 != 0:
            result.append(list[i])
    return result